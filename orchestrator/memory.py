"""
Memory management system for orchestrator agent.

This module handles persistent storage and retrieval of architectural
decisions, patterns, and learned preferences across sessions.
"""

import json
from pathlib import Path
from typing import List, Optional, Dict, Any
from datetime import datetime
from .models import MemoryEntry


class MemoryManager:
    """
    Manages persistent memory for the orchestrator agent.

    Memory is stored as JSON files in the /memories directory and
    accessed via the memory tool during orchestration.
    """

    def __init__(self, memory_dir: Path = Path(".claude/memories")):
        """
        Initialize memory manager.

        Args:
            memory_dir: Directory for storing memory files
        """
        self.memory_dir = memory_dir
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        self.index_file = self.memory_dir / "index.json"
        self._ensure_index()

    def _ensure_index(self) -> None:
        """Ensure the memory index file exists."""
        if not self.index_file.exists():
            self._save_index({})

    def _load_index(self) -> Dict[str, Any]:
        """Load the memory index."""
        with open(self.index_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save_index(self, index: Dict[str, Any]) -> None:
        """Save the memory index."""
        with open(self.index_file, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=2, ensure_ascii=False)

    def store_memory(self, entry: MemoryEntry) -> None:
        """
        Store a memory entry.

        Args:
            entry: Memory entry to store

        Example:
            >>> memory = MemoryEntry(
            ...     key="api_pattern_rest",
            ...     value="Prefer FastAPI over Flask for REST APIs",
            ...     category="architectural_decision",
            ...     timestamp=datetime.now().isoformat()
            ... )
            >>> manager.store_memory(memory)
        """
        # Update index
        index = self._load_index()
        index[entry.key] = {
            "category": entry.category,
            "timestamp": entry.timestamp,
            "relevance_score": entry.relevance_score,
            "file": f"{entry.key}.json"
        }
        self._save_index(index)

        # Store full entry
        entry_file = self.memory_dir / f"{entry.key}.json"
        with open(entry_file, 'w', encoding='utf-8') as f:
            json.dump(entry.model_dump(), f, indent=2, ensure_ascii=False)

    def retrieve_memory(self, key: str) -> Optional[MemoryEntry]:
        """
        Retrieve a specific memory by key.

        Args:
            key: Memory key

        Returns:
            Memory entry or None if not found

        Example:
            >>> memory = manager.retrieve_memory("api_pattern_rest")
            >>> if memory:
            ...     print(memory.value)
        """
        index = self._load_index()
        if key not in index:
            return None

        entry_file = self.memory_dir / index[key]["file"]
        if not entry_file.exists():
            return None

        with open(entry_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return MemoryEntry(**data)

    def search_memories(
        self,
        category: Optional[str] = None,
        min_relevance: float = 0.0
    ) -> List[MemoryEntry]:
        """
        Search memories by category and relevance.

        Args:
            category: Filter by category (None = all categories)
            min_relevance: Minimum relevance score

        Returns:
            List of matching memory entries

        Example:
            >>> decisions = manager.search_memories(
            ...     category="architectural_decision",
            ...     min_relevance=0.8
            ... )
        """
        index = self._load_index()
        results = []

        for key, metadata in index.items():
            if category and metadata["category"] != category:
                continue

            if metadata["relevance_score"] < min_relevance:
                continue

            entry = self.retrieve_memory(key)
            if entry:
                results.append(entry)

        # Sort by relevance score (highest first)
        results.sort(key=lambda e: e.relevance_score, reverse=True)
        return results

    def update_relevance(self, key: str, new_score: float) -> bool:
        """
        Update the relevance score of a memory.

        Args:
            key: Memory key
            new_score: New relevance score (0.0-1.0)

        Returns:
            True if updated, False if not found

        Example:
            >>> # Decay old memories
            >>> manager.update_relevance("old_pattern", 0.5)
        """
        entry = self.retrieve_memory(key)
        if not entry:
            return False

        entry.relevance_score = max(0.0, min(1.0, new_score))
        self.store_memory(entry)
        return True

    def delete_memory(self, key: str) -> bool:
        """
        Delete a memory entry.

        Args:
            key: Memory key to delete

        Returns:
            True if deleted, False if not found
        """
        index = self._load_index()
        if key not in index:
            return False

        # Remove from index
        metadata = index.pop(key)
        self._save_index(index)

        # Delete file
        entry_file = self.memory_dir / metadata["file"]
        if entry_file.exists():
            entry_file.unlink()

        return True

    def get_relevant_context(
        self,
        project_type: str,
        top_k: int = 5
    ) -> str:
        """
        Get relevant memory context for a project type.

        This is used during orchestration to inject learned patterns
        into the conversation.

        Args:
            project_type: Type of project being created
            top_k: Number of top memories to retrieve

        Returns:
            Formatted context string for Claude

        Example:
            >>> context = manager.get_relevant_context("api_automation", top_k=3)
            >>> print(context)
            RELEVANT PATTERNS FROM PREVIOUS PROJECTS:
            1. [architectural_decision] Prefer FastAPI over Flask for REST APIs
            2. [pattern] Use Pydantic for all API request/response models
            ...
        """
        # Get all high-relevance memories
        memories = self.search_memories(min_relevance=0.7)

        # Filter by relevance to project type (simple keyword matching)
        relevant = [
            m for m in memories
            if project_type.lower() in m.value.lower()
            or m.category == "architectural_decision"
        ]

        # Take top K
        top_memories = relevant[:top_k]

        if not top_memories:
            return ""

        # Format context
        lines = ["RELEVANT PATTERNS FROM PREVIOUS PROJECTS:"]
        for i, memory in enumerate(top_memories, 1):
            lines.append(
                f"{i}. [{memory.category}] {memory.value}"
            )

        return "\n".join(lines)

    def store_architectural_decision(
        self,
        decision: str,
        context: str = ""
    ) -> None:
        """
        Store an architectural decision.

        Args:
            decision: The decision made
            context: Additional context about why this decision was made

        Example:
            >>> manager.store_architectural_decision(
            ...     decision="Use asyncio for all I/O operations",
            ...     context="Improves performance for API calls"
            ... )
        """
        key = f"arch_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        value = f"{decision}"
        if context:
            value += f"\nContext: {context}"

        entry = MemoryEntry(
            key=key,
            value=value,
            category="architectural_decision",
            timestamp=datetime.now().isoformat(),
            relevance_score=1.0
        )
        self.store_memory(entry)

    def store_pattern(
        self,
        pattern_name: str,
        pattern_description: str
    ) -> None:
        """
        Store a reusable pattern.

        Args:
            pattern_name: Name of the pattern
            pattern_description: How/when to use this pattern

        Example:
            >>> manager.store_pattern(
            ...     pattern_name="error_handling_decorator",
            ...     pattern_description="Use @handle_errors decorator for all API endpoints"
            ... )
        """
        key = f"pattern_{pattern_name}"
        entry = MemoryEntry(
            key=key,
            value=pattern_description,
            category="pattern",
            timestamp=datetime.now().isoformat(),
            relevance_score=1.0
        )
        self.store_memory(entry)

    def export_memories(self, output_file: Path) -> None:
        """
        Export all memories to a single JSON file.

        Args:
            output_file: Path to output file
        """
        index = self._load_index()
        all_memories = []

        for key in index.keys():
            memory = self.retrieve_memory(key)
            if memory:
                all_memories.append(memory.model_dump())

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(all_memories, f, indent=2, ensure_ascii=False)
