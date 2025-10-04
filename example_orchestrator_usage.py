"""
Example usage of the Orchestrator Agent.

This example demonstrates how to use the OrchestratorAgent to generate
a complete automation project from a simple user request.
"""

import asyncio
from pathlib import Path
from orchestrator import OrchestratorAgent


async def main():
    """
    Main example demonstrating orchestrator usage.
    """

    # Initialize orchestrator
    # Projects will be created in ./generated_projects/
    # Memory will be stored in ./.claude/memories/
    orchestrator = OrchestratorAgent(
        working_dir=Path("./generated_projects"),
        memory_dir=Path("./.claude/memories")
    )

    print("🤖 Claude Agent SDK Orchestrator")
    print("=" * 50)
    print()

    # Example 1: Simple automation request
    print("Example 1: API Task Manager")
    print("-" * 50)

    result = await orchestrator.create_automation(
        user_request="Quiero crear una API REST para gestionar tareas",
        additional_context="Debe incluir autenticación JWT y base de datos SQLite"
    )

    if result.success:
        print(f"✅ Project created successfully!")
        print(f"📁 Location: {result.project_path}")
        print(f"⏱️  Time: {result.execution_time_seconds:.2f}s")
        print(f"📊 Quality Score: {result.validation.quality_score}/10")
        print()

        if result.validation.warnings:
            print("⚠️  Warnings:")
            for warning in result.validation.warnings:
                print(f"   - {warning}")
            print()

        if result.validation.recommendations:
            print("💡 Recommendations:")
            for rec in result.validation.recommendations:
                print(f"   - {rec}")
            print()
    else:
        print(f"❌ Error: {result.error}")
        print()

    # Example 2: Data processing automation
    print("Example 2: PDF Invoice Processor")
    print("-" * 50)

    result2 = await orchestrator.create_automation(
        user_request="Automatizar extracción de datos de facturas PDF",
        additional_context="Procesar múltiples PDFs, extraer campos clave, normalizar formato"
    )

    if result2.success:
        print(f"✅ Project created successfully!")
        print(f"📁 Location: {result2.project_path}")
        print(f"⏱️  Time: {result2.execution_time_seconds:.2f}s")
        print(f"📊 Quality Score: {result2.validation.quality_score}/10")
        print()
    else:
        print(f"❌ Error: {result2.error}")
        print()

    # Example 3: Using memory context
    print("Example 3: Leveraging Learned Patterns")
    print("-" * 50)

    # Store a pattern in memory
    orchestrator.memory.store_pattern(
        pattern_name="fastapi_preference",
        pattern_description="Prefer FastAPI over Flask for API automation projects"
    )

    orchestrator.memory.store_architectural_decision(
        decision="Use Pydantic for all data validation",
        context="Provides better type safety and automatic documentation"
    )

    # Get relevant context
    context = orchestrator.get_memory_context("api_automation")
    print("Learned patterns:")
    print(context)
    print()

    # Example 4: Standalone intent analysis
    print("Example 4: Analyze Intent Without Creating Project")
    print("-" * 50)

    intent = await orchestrator.analyze_intent(
        "Necesito un sistema de notificaciones por email automatizado"
    )

    print(f"📝 Analyzed Intent:")
    print(f"   Project Name: {intent.project_name}")
    print(f"   Type: {intent.project_type}")
    print(f"   Objective: {intent.main_objective}")
    print(f"   Complexity: {intent.complexity_level}")
    print(f"   Duration: {intent.estimated_duration}")
    print(f"   Required Agents: {', '.join(intent.required_agents)}")
    print()

    # Cleanup
    await orchestrator.cleanup()

    print("=" * 50)
    print("✨ All examples completed!")


async def simple_example():
    """
    Simplified example for quick start.
    """
    # Create orchestrator
    orchestrator = OrchestratorAgent()

    # Generate automation project
    result = await orchestrator.create_automation(
        "Automatizar procesamiento de CSVs con validación de datos"
    )

    # Check result
    if result.success:
        print(f"Project created at: {result.project_path}")
    else:
        print(f"Error: {result.error}")


if __name__ == "__main__":
    # Run main example
    asyncio.run(main())

    # Or run simple example:
    # asyncio.run(simple_example())
