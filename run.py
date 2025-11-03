#!/usr/bin/env python3
"""
Roundtable: Multi-Agent Brainstorming System
Entry point for the CLI.
"""

import sys
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))

try:
    from cli import cli
except ImportError:
    from .cli import cli

if __name__ == "__main__":
    cli()

