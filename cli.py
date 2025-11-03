"""
Command-line interface for Roundtable multi-agent discussions.
"""

import click
from rich.console import Console
from rich.panel import Panel
from rich import box
from pathlib import Path

console = Console()


@click.group()
def cli():
    """
    🎯 Roundtable: Multi-Agent Brainstorming System
    
    Multiple AI models discuss a question in rounds, building on each other's ideas.
    """
    pass


@cli.command()
@click.argument("question")
@click.option("--rounds", "-r", default=3, type=int, help="Number of discussion rounds (default: 3)")
@click.option("--temperature", "-t", default=0.7, type=float, help="Temperature for creativity (0.0-1.0, default: 0.7)")
@click.option("--no-moderator", is_flag=True, help="Disable moderator summary")
@click.option("--tools", "-T", is_flag=True, help="Enable external knowledge tools (web, Wikipedia, arXiv)")
@click.option("--quiet", "-q", is_flag=True, help="Minimal output (no progress)")
@click.option("--export", "-e", type=click.Choice(["markdown", "json", "text"]), help="Export format")
@click.option("--output", "-o", type=click.Path(), help="Output file path")
def discuss(question, rounds, temperature, no_moderator, tools, quiet, export, output):
    """
    Conduct a roundtable discussion on a QUESTION.
    
    Examples:
    
        roundtable discuss "What are the key challenges in AI safety?"
        
        roundtable discuss "How can we improve remote team collaboration?" --rounds 5
        
        roundtable discuss "What makes a great leader?" --export markdown -o discussion.md
        
        roundtable discuss "Latest developments in quantum computing?" --tools
    """
    try:
        from .roundtable import Roundtable
    except ImportError:
        from roundtable import Roundtable
    
    try:
        # Initialize roundtable
        roundtable = Roundtable(
            max_rounds=rounds,
            temperature=temperature,
            moderator_enabled=not no_moderator,
            tools_enabled=tools,
        )
        
        if not quiet:
            console.print(Panel(
                f"[bold cyan]Roundtable Discussion[/bold cyan]\n"
                f"Rounds: {rounds} | Temperature: {temperature} | "
                f"Participants: {len(roundtable.participants)}" +
                (f" | Tools: ENABLED ✅" if tools and roundtable.tools else ""),
                box=box.ROUNDED,
            ))
        
        # Conduct discussion
        discussion = roundtable.discuss(question, verbose=not quiet)
        
        # Export if requested
        if export:
            content = roundtable.export_discussion(discussion, format=export)
            
            if output:
                Path(output).write_text(content)
                console.print(f"\n[green]✓ Discussion exported to {output}[/green]")
            else:
                console.print(f"\n[dim]{'-' * 80}[/dim]")
                console.print(content)
        
        if not quiet:
            console.print("\n[green]✓ Discussion complete![/green]")
        
    except Exception as e:
        console.print(f"\n[red]Error: {e}[/red]")
        raise click.Abort()


@cli.command()
def info():
    """Show information about configured models and available tools."""
    try:
        from .llm import get_participant_models
    except ImportError:
        from llm import get_participant_models
    import os
    
    console.print(Panel(
        "[bold cyan]Roundtable Configuration[/bold cyan]",
        box=box.ROUNDED,
    ))
    
    # Participants
    participants = get_participant_models()
    console.print(f"\n[bold]Participants:[/bold] {len(participants)}")
    for i, p in enumerate(participants, 1):
        console.print(f"  {i}. {p['label']}: [cyan]{p['name']}[/cyan]")
    
    # Moderator
    mod_model = os.getenv("MODERATOR_MODEL")
    if mod_model:
        console.print(f"\n[bold]Moderator:[/bold] [cyan]{mod_model}[/cyan]")
    else:
        console.print(f"\n[bold]Moderator:[/bold] [dim]Using default model[/dim]")
    
    console.print()


@cli.command()
def tools_status():
    """Show status of available external knowledge tools."""
    try:
        from .tools import print_tools_status
    except ImportError:
        from tools import print_tools_status
    
    console.print(Panel(
        "[bold cyan]External Knowledge Tools[/bold cyan]",
        box=box.ROUNDED,
    ))
    
    print_tools_status()
    
    console.print("[dim]Enable tools with:[/dim] [cyan]roundtable discuss \"question\" --tools[/cyan]")


@cli.command()
def example():
    """Show example .env configuration."""
    example_config = """
# Example .env configuration for Roundtable

# Participant 1: GPT-4o
MODEL1=gpt-4o
API_KEY1=your-openai-api-key
BASE_URL1=https://api.openai.com/v1

# Participant 2: Claude Sonnet
MODEL2=claude-sonnet-4.5
API_KEY2=your-anthropic-api-key
BASE_URL2=https://api.anthropic.com/v1

# Participant 3: Llama
MODEL3=meta-llama/Llama-3.3-70B-Instruct
API_KEY3=your-friendli-api-key
BASE_URL3=https://api.friendli.ai/serverless/v1

# Participant 4: DeepSeek
MODEL4=deepseek-ai/DeepSeek-V3
API_KEY4=your-friendli-api-key
BASE_URL4=https://api.friendli.ai/serverless/v1

# Moderator (optional, uses DEFAULT_MODEL if not set)
MODERATOR_MODEL=gpt-4o
MODERATOR_API_KEY=your-openai-api-key
MODERATOR_BASE_URL=https://api.openai.com/v1

# Fallback/Default
DEFAULT_MODEL=gpt-4o
DEFAULT_API_KEY=your-openai-api-key
DEFAULT_BASE_URL=https://api.openai.com/v1

# External Tools (optional)
TAVILY_API_KEY=your-tavily-api-key
"""
    
    console.print(Panel(
        example_config,
        title="[bold cyan].env Configuration Example[/bold cyan]",
        box=box.ROUNDED,
    ))


if __name__ == "__main__":
    cli()

