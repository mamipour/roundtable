#!/usr/bin/env python3
"""Test roundtable discussion."""

import sys
from pathlib import Path

# Add to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from roundtable import Roundtable
    
    print("=" * 80)
    print("ROUNDTABLE DISCUSSION TEST")
    print("=" * 80)
    print()
    
    # Initialize
    print("Initializing roundtable...")
    rt = Roundtable(
        max_rounds=4,
        temperature=0.9,
        moderator_enabled=True,
        tools_enabled=False,
    )
    
    print(f"✓ {len(rt.participants)} participants loaded")
    print()
    
    # Discuss
    discussion = rt.discuss("What's the meaning of life?", verbose=True)
    
    print()
    print("=" * 80)
    print("DISCUSSION COMPLETE")
    print("=" * 80)
    
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

