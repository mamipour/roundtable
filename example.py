#!/usr/bin/env python3
"""
Example usage of Roundtable API.

Shows how to use Roundtable programmatically instead of via CLI.
"""

from roundtable import Roundtable


def basic_example():
    """Basic roundtable discussion."""
    print("=" * 80)
    print("EXAMPLE 1: Basic Discussion")
    print("=" * 80)
    
    # Initialize roundtable
    rt = Roundtable(max_rounds=3, temperature=0.7)
    
    # Conduct discussion
    discussion = rt.discuss(
        "What are the most important skills for software engineers in 2025?",
        verbose=True
    )
    
    print(f"\nTotal rounds: {len(discussion.rounds)}")
    print(f"Total contributions: {sum(len(r['contributions']) for r in discussion.rounds)}")


def export_example():
    """Discussion with export to file."""
    print("\n" + "=" * 80)
    print("EXAMPLE 2: Discussion with Export")
    print("=" * 80)
    
    rt = Roundtable(max_rounds=2, temperature=0.6)
    
    discussion = rt.discuss(
        "How can we make online learning more engaging?",
        verbose=False  # Quiet mode
    )
    
    # Export to markdown
    markdown = rt.export_discussion(discussion, format="markdown")
    
    # Save to file
    with open("discussion_example.md", "w") as f:
        f.write(markdown)
    
    print("✓ Discussion exported to discussion_example.md")
    
    # Also export to JSON
    json_output = rt.export_discussion(discussion, format="json")
    with open("discussion_example.json", "w") as f:
        f.write(json_output)
    
    print("✓ Discussion exported to discussion_example.json")


def custom_config_example():
    """Discussion with custom configuration."""
    print("\n" + "=" * 80)
    print("EXAMPLE 3: Custom Configuration")
    print("=" * 80)
    
    # More rounds, no moderator, lower temperature
    rt = Roundtable(
        max_rounds=5,
        temperature=0.3,
        moderator_enabled=False
    )
    
    discussion = rt.discuss(
        "What is the best strategy for technical debt management?",
        verbose=True
    )
    
    # Access discussion data
    print(f"\nFirst round, first contribution:")
    first_contrib = discussion.rounds[0]["contributions"][0]
    print(f"Participant: {first_contrib['participant']}")
    print(f"Model: {first_contrib['model']}")
    print(f"Text: {first_contrib['text'][:100]}...")


def analyze_discussion():
    """Analyze discussion results."""
    print("\n" + "=" * 80)
    print("EXAMPLE 4: Discussion Analysis")
    print("=" * 80)
    
    rt = Roundtable(max_rounds=3)
    
    discussion = rt.discuss(
        "What are the pros and cons of remote work?",
        verbose=False
    )
    
    # Analyze participation
    print("\nParticipation Analysis:")
    for participant in rt.participants:
        contrib_count = len(participant.contributions)
        avg_length = sum(len(c) for c in participant.contributions) / contrib_count
        print(f"\n{participant.label} ({participant.name}):")
        print(f"  Contributions: {contrib_count}")
        print(f"  Avg length: {avg_length:.0f} characters")
    
    # Show summary if available
    if discussion.final_summary:
        print(f"\nFinal Summary Length: {len(discussion.final_summary)} characters")
        print(f"Summary Preview: {discussion.final_summary[:150]}...")


def discussion_with_files():
    """Discussion with data files/directories."""
    print("\n" + "=" * 80)
    print("EXAMPLE 5: Discussion with Data Files")
    print("=" * 80)
    
    # Create sample text files for demonstration
    import tempfile
    import os
    
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create sample files
        file1 = os.path.join(tmpdir, "data1.txt")
        file2 = os.path.join(tmpdir, "data2.txt")
        
        with open(file1, "w") as f:
            f.write("Sample data about AI: Machine learning has revolutionized many industries.")
        
        with open(file2, "w") as f:
            f.write("Economic trends: The tech sector has shown significant growth in recent years.")
        
        # Initialize roundtable with data files
        rt = Roundtable(
            max_rounds=2,
            temperature=0.6,
            data_files=[file1, file2]
        )
        
        # Conduct discussion with file data
        discussion = rt.discuss(
            "What insights can you draw from the provided data?",
            verbose=True
        )
        
        print(f"\n✓ Discussion completed with {len(discussion.file_data)} files")
        print(f"✓ File data was available to all {len(rt.participants)} participants")


if __name__ == "__main__":
    print("Roundtable API Examples\n")
    
    try:
        # Run all examples
        basic_example()
        export_example()
        custom_config_example()
        analyze_discussion()
        discussion_with_files()
        
        print("\n" + "=" * 80)
        print("✓ All examples completed successfully!")
        print("=" * 80)
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nMake sure you have:")
        print("1. Installed dependencies: pip install -r requirements.txt")
        print("2. Configured .env with at least MODEL1 and API_KEY1")
        print("3. Valid API credentials")

