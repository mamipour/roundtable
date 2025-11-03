# Contributing to Roundtable

Thank you for your interest in contributing to Roundtable! We welcome contributions from the community.

## 🎯 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected vs. actual behavior**
- **Environment details** (OS, Python version, dependencies)
- **Configuration** (sanitized .env details, model names)
- **Error messages** or logs

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide detailed description** of the suggested enhancement
- **Explain why this would be useful** to most Roundtable users
- **List any similar features** in other tools (if applicable)

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** with clear, descriptive commits
3. **Test thoroughly** - run `python run_test.py`
4. **Update documentation** if needed
5. **Follow code style** guidelines (see below)
6. **Submit a pull request** with a clear description

## 🛠️ Development Setup

```bash
# Fork and clone the repository
git clone https://github.com/mamipour/roundtable.git
cd roundtable

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure .env for testing
cp env.template .env
# Edit .env with your test API keys

# Run tests
python run_test.py

# Test CLI commands
python run.py info
python run.py discuss "Test question"
```

## 📝 Code Style Guidelines

### Python Style

- Follow **PEP 8** guidelines
- Use **4 spaces** for indentation (no tabs)
- Maximum line length: **88 characters** (Black formatter standard)
- Use **type hints** where appropriate
- Write **docstrings** for all public functions and classes

### Documentation Style

```python
def example_function(param1: str, param2: int) -> bool:
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of param1
        param2: Description of param2
    
    Returns:
        Description of return value
    
    Raises:
        ValueError: When param2 is negative
    """
    pass
```

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- First line should be concise (50 chars or less)
- Reference issues and pull requests when relevant

Good commit messages:
```
Add web search integration for tools
Fix: Resolve API key validation error
Update README with new examples
Refactor: Simplify participant initialization
```

## 🧪 Testing

Before submitting a PR:

```bash
# Run the test suite
python run_test.py

# Test various CLI commands
python run.py info
python run.py tools-status
python run.py discuss "Test question" --rounds 2

# Test with different configurations
# (1 participant, multiple participants, with/without tools)
```

## 📁 Project Structure

```
roundtable/
├── __init__.py           # Package initialization
├── llm.py                # LLM client configuration
├── roundtable.py         # Core discussion engine
├── tools.py              # External knowledge tools
├── cli.py                # Command-line interface
├── run.py                # Entry point
├── run_test.py           # Test script
├── requirements.txt      # Dependencies
├── env.template          # Configuration template
├── README.md             # Main documentation
├── QUICKSTART.md         # Quick start guide
├── CONTRIBUTING.md       # This file
└── LICENSE               # MIT license
```

## 🔍 Key Areas for Contribution

### High Priority

- **Additional LLM providers**: Add support for more OpenAI-compatible APIs
- **Enhanced tools**: New external knowledge sources
- **Testing**: Unit tests, integration tests
- **Documentation**: Examples, tutorials, use cases
- **Error handling**: Better error messages and recovery

### Medium Priority

- **Export formats**: Additional output formats (HTML, PDF)
- **Visualization**: Discussion flow diagrams, statistics
- **Performance**: Async operations, caching
- **Configuration**: YAML/TOML config support

### Ideas Welcome

- New features you think would be useful
- Performance improvements
- Better UX/UI in the terminal
- Integration with other tools

## 📋 Pull Request Checklist

Before submitting your PR, ensure:

- [ ] Code follows the style guidelines
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Documentation updated
- [ ] Commit messages are clear
- [ ] No merge conflicts
- [ ] Self-review completed

## 🤝 Code of Conduct

### Our Pledge

We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards

**Positive behavior includes:**
- Using welcoming and inclusive language
- Being respectful of differing viewpoints
- Gracefully accepting constructive criticism
- Focusing on what is best for the community

**Unacceptable behavior includes:**
- Harassment, trolling, or derogatory comments
- Public or private harassment
- Publishing others' private information
- Other conduct inappropriate in a professional setting

## 📞 Questions?

- **General questions**: Open a [GitHub Discussion](https://github.com/mamipour/roundtable/discussions)
- **Bug reports**: Open a [GitHub Issue](https://github.com/mamipour/roundtable/issues)
- **Security issues**: Email [f.mamipour@example.com](mailto:f.mamipour@example.com)

## 🎉 Recognition

Contributors will be:
- Listed in project contributors
- Mentioned in release notes for significant contributions
- Given credit in relevant documentation

Thank you for contributing to Roundtable! 🚀

