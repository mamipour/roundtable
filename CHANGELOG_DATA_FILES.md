# Changelog: Data Files Feature

## Summary

Added comprehensive support for passing text files and directories to Roundtable discussions. All AI agents can now access file contents during discussions, enabling data analysis, document comparison, and content summarization.

## Version: Data Files Feature v1.0

**Date**: November 3, 2025

## What's New

### Core Features

- ✅ **File Loading**: Support for individual text files
- ✅ **Directory Loading**: Recursive scanning of directories for text files
- ✅ **Multiple Sources**: Mix and match files and directories
- ✅ **File Types**: Support for `.txt`, `.md`, `.csv`, `.json`, `.text` files
- ✅ **CLI Integration**: New `--data` / `-d` flag (can be used multiple times)
- ✅ **Python API**: New `data_files` parameter in Roundtable class
- ✅ **File Metadata**: Agents receive filename, path, content, and size
- ✅ **Error Handling**: Graceful handling of missing/unreadable files

### Files Modified

1. **roundtable.py** (Core implementation)
   - Added `data_files` parameter to `__init__`
   - Added `file_data` field to Discussion dataclass
   - Implemented `_load_text_file()` static method
   - Implemented `_load_data_files()` method
   - Updated `discuss()` to load and display files
   - Updated `_create_participant_prompt()` to include file content
   - Updated `_conduct_round()` to pass file data

2. **cli.py** (CLI interface)
   - Added `--data` / `-d` option with multiple=True
   - Updated info panel to show data files count
   - Updated examples in docstring

3. **example.py** (API examples)
   - Added `discussion_with_files()` function
   - Demonstrates file loading and usage
   - Integrated into main example runner

4. **README.md** (Documentation)
   - Added "Data Files Feature" section
   - Updated Features list
   - Added to Quick Start section
   - Updated Advanced Options
   - Added Data Analysis use case
   - Updated Python API examples

5. **QUICKSTART.md** (Quick start guide)
   - Added data files examples to options section
   - Added new section explaining the feature
   - Included supported file types

### Files Created

1. **test_data_files.py**
   - Comprehensive test script
   - Tests single file, directory, and mixed usage
   - Creates sample data for testing
   - Validates feature functionality

2. **DATA_FILES_FEATURE.md**
   - Complete feature documentation
   - Technical implementation details
   - Usage examples and patterns
   - Future enhancement ideas

3. **USAGE_EXAMPLES.md**
   - Extensive usage examples
   - Real-world scenarios
   - Best practices and tips
   - Troubleshooting guide

4. **CHANGELOG_DATA_FILES.md** (this file)
   - Complete changelog
   - Migration guide
   - Breaking changes (none)

## Technical Details

### API Changes

#### Roundtable Class

**New Parameter**:
```python
Roundtable(
    max_rounds: int = 3,
    temperature: float = 0.7,
    moderator_enabled: bool = True,
    tools_enabled: bool = False,
    data_files: Optional[List[str]] = None,  # NEW
)
```

**New Methods**:
- `_load_text_file(file_path: Path) -> Optional[Dict]` - Load single file
- `_load_data_files() -> List[Dict]` - Load all files from paths

**Modified Methods**:
- `discuss()` - Now loads files and passes to rounds
- `_create_participant_prompt()` - Includes file content in prompts
- `_conduct_round()` - Passes file data to prompt creation

#### Discussion Class

**New Field**:
```python
@dataclass
class Discussion:
    question: str
    rounds: List[Dict] = field(default_factory=list)
    final_summary: Optional[str] = None
    file_data: Optional[List[Dict]] = None  # NEW
```

### CLI Changes

**New Option**:
```bash
--data, -d PATH    File or directory containing text files
                   (can be used multiple times)
```

**Examples**:
```bash
python run.py discuss "Question" --data file.txt
python run.py discuss "Question" --data dir1 --data dir2
```

### Data Structure

Each file is represented as:
```python
{
    'filename': str,   # Just the filename
    'path': str,       # Full path
    'content': str,    # Complete file content
    'size': int        # Character count
}
```

## Usage Examples

### CLI Usage

```bash
# Single file
python run.py discuss "Summarize this" --data report.txt

# Multiple files
python run.py discuss "Compare these" --data file1.txt --data file2.txt

# Directory
python run.py discuss "Analyze all" --data ./data_dir

# Mixed
python run.py discuss "Complete analysis" --data file.txt --data ./dir
```

### Python API Usage

```python
from roundtable import Roundtable

# Initialize with files
rt = Roundtable(
    max_rounds=3,
    data_files=['file.txt', './dir']
)

# Conduct discussion
discussion = rt.discuss("What insights do you see?")

# Access file data
for file in discussion.file_data:
    print(f"{file['filename']}: {file['size']} chars")
```

## Breaking Changes

**None** - This is a purely additive feature. All existing code continues to work without modification.

## Migration Guide

### If You're Already Using Roundtable

No changes needed! The feature is completely optional:

```python
# Old code - still works exactly the same
rt = Roundtable(max_rounds=3)
discussion = rt.discuss("Question")

# New code - with data files
rt = Roundtable(max_rounds=3, data_files=['data.txt'])
discussion = rt.discuss("Question about data")
```

### Updating Your Workflows

If you want to add data file support:

**Before**:
```bash
python run.py discuss "Analyze market trends" --rounds 4
```

**After**:
```bash
python run.py discuss "Analyze market trends" --data market_data.txt --rounds 4
```

## Compatibility

- ✅ Python 3.8+
- ✅ All existing features (tools, export, moderator)
- ✅ All AI model providers
- ✅ All export formats (markdown, json, text)

## Performance

- File loading is synchronous during `discuss()` call
- All files loaded into memory
- No significant performance impact for typical use cases
- Consider file sizes for very large datasets

## Security

- Files are read with UTF-8 encoding only
- No code execution from files
- Paths are validated before loading
- Errors are caught and reported

## Testing

Run tests with:
```bash
python test_data_files.py
```

This validates:
- ✅ Single file loading
- ✅ Directory scanning
- ✅ Mixed file/directory usage
- ✅ File metadata extraction
- ✅ Error handling

## Known Limitations

1. Only text-based files supported (no binary files)
2. Files must be UTF-8 encoded
3. Very large files may exceed context limits
4. No automatic file size limits (use discretion)

## Future Enhancements

Potential improvements for future releases:

- [ ] PDF file support
- [ ] Image OCR support  
- [ ] Automatic chunking for large files
- [ ] File size warnings/limits
- [ ] Support for more formats (XML, HTML, etc.)
- [ ] File filtering by pattern/regex
- [ ] Streaming for very large files
- [ ] File content caching
- [ ] Compression for large text files

## Support

For issues or questions:
- Check `DATA_FILES_FEATURE.md` for detailed documentation
- See `USAGE_EXAMPLES.md` for usage patterns
- Run `python run.py discuss --help` for CLI help
- Check GitHub issues for known problems

## Credits

Feature designed and implemented to enable multi-agent document analysis and data-driven discussions.

## Related Documentation

- `README.md` - Main project documentation
- `QUICKSTART.md` - Getting started guide
- `DATA_FILES_FEATURE.md` - Detailed feature docs
- `USAGE_EXAMPLES.md` - Usage examples and patterns
- `example.py` - Python API examples

## Acknowledgments

This feature enables new use cases:
- 📊 Data analysis and interpretation
- 📝 Document comparison and synthesis
- 🔍 Content extraction and summarization
- 💼 Business intelligence from text data
- 🎓 Research paper analysis
- 📈 Report generation from raw data

---

**Feature Status**: ✅ Complete and Production Ready

**Testing Status**: ✅ Tested and Validated

**Documentation Status**: ✅ Fully Documented

