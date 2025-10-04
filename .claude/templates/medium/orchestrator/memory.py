"""
{{ project_name }} - Memory Manager

Persistent memory system for learning and context retention.
"""

import json
import uuid
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
import logging

from .models import MemoryEntry, WorkflowIntent

logger = logging.getLogger(__name__)


class MemoryManager:
    """
    Manages persistent memory for the orchestrator.

    Stores and retrieves execution history, decisions, and patterns.
    """

    def __init__(self, memory_dir: Path):
        """
        Initialize memory manager.

        Args:
            memory_dir: Directory for storing memory files
        """
        self.memory_dir = Path(memory_dir)
        self.memory_dir.mkdir(parents=True, exist_ok=True)
        self.memory_file = self.memory_dir / "executions.json"

        # Initialize memory file if it doesn't exist
        if not self.memory_file.exists():
            self._save_memories([])

        logger.info(f"Memory manager initialized: {self.memory_dir}")

    def _load_memories(self) -> List[Dict[str, Any]]:
        """Load all memories from file."""
        try:
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading memories: {e}")
            return []

    def _save_memories(self, memories: List[Dict[str, Any]]):
        """Save memories to file."""
        try:
            with open(self.memory_file, 'w') as f:
                json.dump(memories, f, indent=2, default=str)
        except Exception as e:
            logger.error(f"Error saving memories: {e}")

    async def store_execution(
        self,
        intent: WorkflowIntent,
        result: Dict[str, Any]
    ) -> str:
        """
        Store a workflow execution in memory.

        Args:
            intent: The workflow intent that was executed
            result: The execution result

        Returns:
            Memory entry ID
        """
        entry_id = f"exec_{uuid.uuid4().hex[:8]}"

        memory_entry = {
            "id": entry_id,
            "type": "execution",
            "content": {
                "intent": intent.model_dump(),
                "result": result
            },
            "relevance_score": 1.0,
            "timestamp": datetime.now().isoformat(),
            "tags": ["execution", "{{ project_name }}"]
        }

        memories = self._load_memories()
        memories.append(memory_entry)

        # Keep only last 100 memories to avoid file growing too large
        memories = memories[-100:]

        self._save_memories(memories)
        logger.info(f"Stored execution memory: {entry_id}")

        return entry_id

    async def store_decision(
        self,
        decision: str,
        context: Dict[str, Any],
        reasoning: str
    ) -> str:
        """
        Store an architectural or workflow decision.

        Args:
            decision: The decision made
            context: Context in which decision was made
            reasoning: Reasoning behind the decision

        Returns:
            Memory entry ID
        """
        entry_id = f"decision_{uuid.uuid4().hex[:8]}"

        memory_entry = {
            "id": entry_id,
            "type": "decision",
            "content": {
                "decision": decision,
                "context": context,
                "reasoning": reasoning
            },
            "relevance_score": 1.0,
            "timestamp": datetime.now().isoformat(),
            "tags": ["decision", "{{ project_name }}"]
        }

        memories = self._load_memories()
        memories.append(memory_entry)
        self._save_memories(memories)

        logger.info(f"Stored decision memory: {entry_id}")
        return entry_id

    async def get_context(
        self,
        query: Optional[str] = None,
        max_results: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Retrieve relevant context from memory.

        Args:
            query: Optional query to filter memories
            max_results: Maximum number of results to return

        Returns:
            List of relevant memory entries
        """
        memories = self._load_memories()

        # Apply relevance decay (older memories are less relevant)
        current_time = datetime.now()
        for memory in memories:
            memory_time = datetime.fromisoformat(memory['timestamp'])
            days_old = (current_time - memory_time).days

            # Decay relevance by 10% per week
            decay_factor = 0.9 ** (days_old / 7)
            memory['relevance_score'] *= decay_factor

        # Sort by relevance score (descending)
        memories.sort(key=lambda m: m['relevance_score'], reverse=True)

        # Filter by query if provided
        if query:
            filtered = []
            query_lower = query.lower()
            for memory in memories:
                content_str = json.dumps(memory['content']).lower()
                if query_lower in content_str or any(query_lower in tag for tag in memory.get('tags', [])):
                    filtered.append(memory)
            memories = filtered

        return memories[:max_results]

    async def clear_old_memories(self, days: int = 30):
        """
        Clear memories older than specified days.

        Args:
            days: Clear memories older than this many days
        """
        memories = self._load_memories()
        cutoff_date = datetime.now() - timedelta(days=days)

        filtered_memories = [
            m for m in memories
            if datetime.fromisoformat(m['timestamp']) > cutoff_date
        ]

        removed_count = len(memories) - len(filtered_memories)
        self._save_memories(filtered_memories)

        logger.info(f"Cleared {removed_count} old memories (>{days} days)")
        return removed_count
