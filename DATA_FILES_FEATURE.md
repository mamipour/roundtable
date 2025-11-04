# Data Files Feature Documentation

## Overview

The Data Files feature allows you to pass text files or directories to Roundtable discussions, making their contents available to all AI agents. This enables data analysis, document comparison, and content summarization through multi-agent collaboration.

## Features

- ✅ Support for single files or entire directories
- ✅ Multiple file types: `.txt`, `.md`, `.csv`, `.json`, `.text`
- ✅ Recursive directory scanning
- ✅ All agents see both filenames and full content
- ✅ Works with CLI and Python API
- ✅ Combines with existing tools (web search, Wikipedia, arXiv)

## Usage

### Command Line Interface

#### Single File
```bash
python run.py discuss "Summarize this report" --data ./report.txt
```

#### Multiple Files
```bash
python run.py discuss "Compare these documents" --data ./doc1.txt --data ./doc2.md
```

#### Directory
```bash
python run.py discuss "What patterns exist in this data?" --data ./data_directory
```

#### Mixed
```bash
python run.py discuss "Analyze everything" --data ./file.txt --data ./folder
```

### Python API

```python
from roundtable import Roundtable

# Initialize with data files
rt = Roundtable(
    max_rounds=3,
    temperature=0.7,
    data_files=['./data.txt', './reports_dir']
)

# Conduct discussion
discussion = rt.discuss("What insights can you find?")

# Access file metadata
if discussion.file_data:
    print(f"Loaded {len(discussion.file_data)} files")
    for file in discussion.file_data:
        print(f"  - {file['filename']}: {file['size']} chars")
```

## Implementation Details

### Files Modified

1. **roundtable.py**
   - Added `data_files` parameter to `Roundtable.__init__()`
   - Added `file_data` field to `Discussion` dataclass
   - Added `_load_text_file()` static method
   - Added `_load_data_files()` method
   - Updated `discuss()` to load and display files
   - Updated `_create_participant_prompt()` to include file content
   - Updated `_conduct_round()` to pass file data to prompts

2. **cli.py**
   - Added `--data` / `-d` option (can be used multiple times)
   - Updated discussion panel to show data files count
   - Updated examples in docstring

3. **example.py**
   - Added `discussion_with_files()` example function
   - Updated main to run the new example

4. **README.md**
   - Added Data Files Feature section with examples
   - Updated Features list
   - Updated Advanced Options section
   - Added Data Analysis use case
   - Updated Python API section

5. **QUICKSTART.md**
   - Added data files examples
   - Added new section explaining the feature

### New Files

1. **test_data_files.py**
   - Comprehensive test script
   - Creates sample files
   - Tests single file, directory, and mixed usage
   - Demonstrates all use cases

2. **DATA_FILES_FEATURE.md** (this file)
   - Complete documentation
   - Usage examples
   - Implementation details

## Technical Details

### File Loading Process

1. User provides file/directory paths via CLI or API
2. `_load_data_files()` processes each path:
   - If file: loads directly
   - If directory: recursively finds all supported text files
3. `_load_text_file()` reads each file:
   - Reads content with UTF-8 encoding
   - Creates metadata dict with filename, path, content, size
4. File data stored in `Discussion.file_data`
5. Content added to participant prompts via `_create_participant_prompt()`

### Data Structure

Each loaded file is represented as:
```python
{
    'filename': 'example.txt',      # Just the filename
    'path': '/full/path/to/file',   # Full path
    'content': '...',               # Complete file content
    'size': 1234                    # Character count
}
```

### Prompt Integration

File content is prepended to the user message in each round:
```
📁 AVAILABLE DATA FILES:
You have access to the following files for reference:

--- FILE: example.txt ---
[file content here]

--- FILE: data.md ---
[file content here]
```

## Use Cases

### Document Analysis
```bash
python run.py discuss "What are the main themes?" --data ./research_paper.txt
```

### Data Comparison
```bash
python run.py discuss "How do Q1 and Q2 differ?" --data ./q1_report.txt --data ./q2_report.txt
```

### Bulk Analysis
```bash
python run.py discuss "Summarize all customer feedback" --data ./feedback_dir
```

### Mixed Media
```bash
python run.py discuss "Synthesize insights" --data ./report.md --data ./data.csv --data ./notes_dir
```

## Testing

Run the test script to verify the feature:
```bash
python test_data_files.py
```

This will:
1. Create sample text files
2. Test single file loading
3. Test directory loading
4. Test mixed file/directory loading
5. Verify file data is available to agents

## Compatibility

- ✅ Works with all AI models/providers
- ✅ Combines with `--tools` flag
- ✅ Combines with `--export` flag
- ✅ Works in both verbose and quiet modes
- ✅ Compatible with moderator feature

## Limitations

- Only text-based files are supported
- Files must be UTF-8 encoded
- Very large files may exceed context limits
- Binary files are not supported

## Future Enhancements

Possible improvements for future versions:
- Support for PDF files
- Automatic text extraction from images (OCR)
- File content summarization for large files
- Chunk-based loading for very large datasets
- Support for more file formats (XML, HTML, etc.)
- File filtering by pattern/regex
- Maximum file size limits with warnings

## Error Handling

The feature includes robust error handling:
- Non-existent paths: Warning printed, continues with other files
- Unreadable files: Warning printed, skips file
- Empty files: Loaded but content is empty string
- Invalid encodings: Error caught and reported

## Performance

- File loading is synchronous during initialization
- All file content is loaded into memory
- Large directories may take time to scan
- Consider file sizes when working with many/large files

## Related Documentation

- See `README.md` for full project documentation
- See `QUICKSTART.md` for quick start guide
- See `example.py` for Python API examples
- Run `python run.py discuss --help` for CLI help

