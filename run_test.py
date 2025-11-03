#!/usr/bin/env python3
"""Run roundtable discussion test."""

import sys
import os
from pathlib import Path

# Ensure we're in the right directory
os.chdir(Path(__file__).parent)
sys.path.insert(0, str(Path(__file__).parent))

print("=" * 80)
print("ROUNDTABLE: What's the meaning of life?")
print("=" * 80)
print()

try:
    # Check dependencies
    print("Checking dependencies...")
    try:
        import click
        import rich
        from langchain_openai import ChatOpenAI
        from dotenv import load_dotenv
        print("✓ Dependencies loaded")
    except ImportError as e:
        print(f"✗ Missing dependency: {e}")
        print("\nInstall with: pip install -r requirements.txt")
        sys.exit(1)
    
    # Load .env
    print("Loading .env...")
    env_path = Path(__file__).parent / ".env"
    if not env_path.exists():
        print(f"✗ .env not found at: {env_path}")
        sys.exit(1)
    
    load_dotenv(env_path)
    print("✓ .env loaded")
    print()
    
    # Check API keys
    print("Checking API keys...")
    api_keys = {
        'API_KEY1': os.getenv('API_KEY1'),
        'API_KEY2': os.getenv('API_KEY2'),
        'API_KEY3': os.getenv('API_KEY3'),
        'API_KEY4': os.getenv('API_KEY4'),
    }
    
    for key, value in api_keys.items():
        if value:
            print(f"✓ {key}: {value[:15]}...")
        else:
            print(f"✗ {key}: NOT SET")
    print()
    
    # Import and run
    print("Initializing roundtable...")
    from roundtable import Roundtable
    
    rt = Roundtable(
        max_rounds=4,
        temperature=0.9,
        moderator_enabled=True,
        tools_enabled=False,
    )
    
    print(f"✓ Loaded {len(rt.participants)} participants:")
    for p in rt.participants:
        print(f"  - {p.label}: {p.name}")
    print()
    print("=" * 80)
    print()
    
    # Run discussion
    discussion = rt.discuss("What's the meaning of life?", verbose=True)
    
    print()
    print("=" * 80)
    print("✓ DISCUSSION COMPLETE")
    print("=" * 80)
    
except Exception as e:
    print()
    print("=" * 80)
    print(f"✗ ERROR: {e}")
    print("=" * 80)
    import traceback
    traceback.print_exc()
    sys.exit(1)

