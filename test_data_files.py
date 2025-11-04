#!/usr/bin/env python3
"""
Test script to demonstrate data files feature.
Creates sample text files and runs a discussion with them.
"""

import tempfile
import os
from pathlib import Path

def create_sample_files(tmpdir):
    """Create sample text files for testing."""
    # Create a subdirectory
    data_dir = Path(tmpdir) / "data"
    data_dir.mkdir(exist_ok=True)
    
    # Sample file 1: AI trends
    file1 = data_dir / "ai_trends.txt"
    file1.write_text("""
AI Industry Trends 2025

Key observations:
- Large Language Models continue to dominate the AI landscape
- Multi-agent systems are gaining traction for complex problem-solving
- AI ethics and safety remain critical concerns
- Open-source models are challenging proprietary solutions
- Enterprise adoption is accelerating across all sectors
""")
    
    # Sample file 2: Market data
    file2 = data_dir / "market_data.txt"
    file2.write_text("""
Technology Market Analysis Q1 2025

Findings:
- AI market valued at $500B+ globally
- 70% of Fortune 500 companies have AI initiatives
- Investment in AI infrastructure up 45% YoY
- Developer tools and platforms fastest growing segment
- Concerns about AI regulation impacting growth
""")
    
    # Sample file 3: Customer feedback
    file3 = tmpdir / "feedback.txt"
    file3.write_text("""
Customer Feedback Summary

Positive:
- AI tools are saving significant time
- Easy integration with existing workflows
- Good accuracy on most tasks

Areas for improvement:
- Need better documentation
- Some features are hard to discover
- Pricing could be more flexible
""")
    
    return str(data_dir), str(file3)


def test_single_file():
    """Test with a single file."""
    print("\n" + "="*80)
    print("TEST 1: Single File")
    print("="*80)
    
    try:
        from roundtable import Roundtable
    except ImportError:
        print("❌ Error: Could not import roundtable. Make sure it's installed.")
        return
    
    with tempfile.TemporaryDirectory() as tmpdir:
        _, feedback_file = create_sample_files(tmpdir)
        
        print(f"\n📁 Testing with single file: {Path(feedback_file).name}")
        
        rt = Roundtable(
            max_rounds=2,
            temperature=0.7,
            moderator_enabled=True,
            data_files=[feedback_file]
        )
        
        discussion = rt.discuss(
            "Based on the customer feedback, what are the top 3 priorities?",
            verbose=True
        )
        
        if discussion.file_data:
            print(f"\n✅ Success! Loaded {len(discussion.file_data)} file(s)")
            for f in discussion.file_data:
                print(f"   - {f['filename']}: {f['size']} characters")
        else:
            print("\n❌ Failed: No file data loaded")


def test_directory():
    """Test with a directory of files."""
    print("\n" + "="*80)
    print("TEST 2: Directory of Files")
    print("="*80)
    
    try:
        from roundtable import Roundtable
    except ImportError:
        print("❌ Error: Could not import roundtable. Make sure it's installed.")
        return
    
    with tempfile.TemporaryDirectory() as tmpdir:
        data_dir, _ = create_sample_files(tmpdir)
        
        print(f"\n📁 Testing with directory: {Path(data_dir).name}")
        
        rt = Roundtable(
            max_rounds=2,
            temperature=0.7,
            moderator_enabled=True,
            data_files=[data_dir]
        )
        
        discussion = rt.discuss(
            "What trends and patterns do you see across all the data files?",
            verbose=True
        )
        
        if discussion.file_data:
            print(f"\n✅ Success! Loaded {len(discussion.file_data)} file(s)")
            for f in discussion.file_data:
                print(f"   - {f['filename']}: {f['size']} characters")
        else:
            print("\n❌ Failed: No file data loaded")


def test_mixed():
    """Test with both files and directories."""
    print("\n" + "="*80)
    print("TEST 3: Mixed Files and Directories")
    print("="*80)
    
    try:
        from roundtable import Roundtable
    except ImportError:
        print("❌ Error: Could not import roundtable. Make sure it's installed.")
        return
    
    with tempfile.TemporaryDirectory() as tmpdir:
        data_dir, feedback_file = create_sample_files(tmpdir)
        
        print(f"\n📁 Testing with directory + file")
        
        rt = Roundtable(
            max_rounds=2,
            temperature=0.7,
            moderator_enabled=True,
            data_files=[data_dir, feedback_file]
        )
        
        discussion = rt.discuss(
            "Synthesize insights from all available data sources.",
            verbose=True
        )
        
        if discussion.file_data:
            print(f"\n✅ Success! Loaded {len(discussion.file_data)} file(s)")
            total_chars = sum(f['size'] for f in discussion.file_data)
            print(f"   Total content: {total_chars:,} characters")
            for f in discussion.file_data:
                print(f"   - {f['filename']}: {f['size']:,} characters")
        else:
            print("\n❌ Failed: No file data loaded")


def main():
    """Run all tests."""
    print("\n" + "="*80)
    print("🧪 Roundtable Data Files Feature Tests")
    print("="*80)
    
    try:
        test_single_file()
        test_directory()
        test_mixed()
        
        print("\n" + "="*80)
        print("✅ All tests completed!")
        print("="*80)
        print("\nNote: These tests require configured AI models in .env")
        print("See README.md for configuration instructions.")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you have:")
        print("1. Configured .env with at least MODEL1 and API_KEY1")
        print("2. Valid API credentials")
        print("3. Installed all dependencies: pip install -r requirements.txt")


if __name__ == "__main__":
    main()

