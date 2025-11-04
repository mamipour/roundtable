# 🎯 Roundtable: Multi-Agent AI Brainstorming System

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![LangChain](https://img.shields.io/badge/LangChain-Powered-green.svg)](https://python.langchain.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

> **Collaborative AI discussions at scale** - Where multiple AI models engage in structured roundtable discussions, building on each other's ideas to produce well-reasoned, comprehensive insights.

Roundtable is a LangChain-powered multi-agent discussion system that orchestrates collaborative brainstorming sessions between different AI models (GPT-4, Claude, Llama, DeepSeek, etc.). Perfect for research, decision-making, creative brainstorming, and exploring complex topics from multiple AI perspectives.

---

## 🌟 Why Roundtable?

- 🧠 **Collective Intelligence**: Leverage multiple AI models simultaneously for richer, more balanced perspectives
- 🔄 **Iterative Refinement**: Ideas evolve and improve across multiple discussion rounds
- 🌐 **Universal Compatibility**: Works with any OpenAI-compatible API (OpenAI, Anthropic, Friendli AI, local models)
- 🔧 **Knowledge-Enhanced**: Integrates web search, Wikipedia, and arXiv for fact-based discussions
- 📊 **Production-Ready**: Export discussions in Markdown, JSON, or plain text
- 🎨 **Beautiful CLI**: Rich terminal interface for an excellent user experience
- ⚡ **Fast Setup**: Configure and run in under 2 minutes

---

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration)
- [Usage Examples](#-usage-examples)
- [External Knowledge Tools](#-external-knowledge-tools)
- [API Support](#-api-support)
- [Use Cases](#-use-cases)
- [Python API](#-python-api)
- [Example Output](#-example-output)
- [Tips for Better Discussions](#-tips-for-better-discussions)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- 🤖 **Multi-Agent Discussion**: Configure 1-N AI models as participants (GPT-4, Claude, Llama, DeepSeek, etc.)
- 🔄 **Round-Based Brainstorming**: Ideas evolve and build across multiple discussion rounds
- 🎙️ **Optional Moderator**: Intelligent AI moderator synthesizes final summaries and key insights
- 🌐 **Universal API Support**: Works with any OpenAI-compatible API endpoint
- 📁 **Data Files Support**: Pass text files or directories for agents to analyze and discuss
- 📊 **Export Options**: Save discussions in Markdown, JSON, or plain text formats
- 🎨 **Rich CLI Interface**: Beautiful, colorful terminal interface powered by `rich`
- 🔧 **External Knowledge Tools**: Integrated web search (Tavily), Wikipedia, and arXiv for research-driven discussions
- 🎯 **Customizable Parameters**: Control rounds, temperature, and participant behavior
- 🔒 **Secure**: API keys stored locally in `.env` file
- 📝 **Conversation Context**: Each participant sees and builds upon others' contributions

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- API keys for your chosen AI providers

### Setup

```bash
# Clone the repository
git clone https://github.com/mamipour/roundtable.git
cd roundtable

# Install dependencies
pip install -r requirements.txt

# Configure your AI models
cp env.template .env

# Edit .env and add your API keys
nano .env  # or use your preferred editor
```

### Verify Installation

```bash
# Check configuration
python run.py info

# Check available tools
python run.py tools-status
```

---

## 🎬 Quick Start

### 1. Basic Discussion (2 Minutes Setup)

```bash
# Minimal setup - just add one API key to .env
MODEL1=gpt-4o
API_KEY1=your-openai-api-key
BASE_URL1=https://api.openai.com/v1

# Run your first discussion
python run.py discuss "What are the key challenges in AI safety?"
```

### 2. Multi-Agent Discussion

```bash
# Configure multiple models in .env, then run:
python run.py discuss "What is the future of renewable energy?" --rounds 4
```

### 3. Knowledge-Enhanced Discussions

```bash
# Enable web search, Wikipedia, and arXiv access
python run.py discuss "Latest developments in quantum computing?" --tools

# Check which tools are available
python run.py tools-status
```

### 4. Discussions with Data Files

```bash
# Provide text files or directories for agents to analyze
python run.py discuss "What insights can you draw from this data?" --data ./data_dir

# Multiple files or directories
python run.py discuss "Analyze these documents" --data ./file1.txt --data ./file2.txt --data ./reports_dir
```

---

## ⚙️ Configuration

Configure AI participants in your `.env` file. The system supports 1-N participants.

### Basic Configuration (Minimum)

```env
# At minimum, configure one participant
MODEL1=gpt-4o
API_KEY1=your-openai-api-key
BASE_URL1=https://api.openai.com/v1
```

### Multi-Agent Configuration (Recommended)

```env
# Participant 1: OpenAI GPT-4o
MODEL1=gpt-4o
API_KEY1=your-openai-api-key
BASE_URL1=https://api.openai.com/v1

# Participant 2: Anthropic Claude Sonnet 4
MODEL2=claude-sonnet-4-20250514
API_KEY2=your-anthropic-api-key
BASE_URL2=https://api.anthropic.com/v1

# Participant 3: Meta Llama 3.3 (via Friendli AI)
MODEL3=meta-llama-3.3-70b-instruct
API_KEY3=your-friendli-api-key
BASE_URL3=https://api.friendli.ai/serverless/v1

# Participant 4: DeepSeek R1 (via Friendli AI)
MODEL4=deepseek-ai/DeepSeek-R1-0528
API_KEY4=your-friendli-api-key
BASE_URL4=https://api.friendli.ai/serverless/v1

# Optional: Moderator (synthesizes final summary)
MODERATOR_MODEL=gpt-4o
MODERATOR_API_KEY=your-openai-api-key
MODERATOR_BASE_URL=https://api.openai.com/v1

# Optional: External Knowledge Tools
TAVILY_API_KEY=your-tavily-api-key  # For web search
# Wikipedia and ArXiv require no API keys
```

### Configuration Tips

- **Minimum Setup**: Just `MODEL1`, `API_KEY1`, and `BASE_URL1`
- **Add Participants**: Continue with `MODEL2`, `MODEL3`, etc. (no limit)
- **Mix Providers**: Combine OpenAI, Anthropic, local models, etc.
- **Moderator**: Optional but recommended for complex discussions
- **Tools**: Optional - adds research capabilities

---

## 📁 Data Files Feature

Roundtable can load text files or directories and make them available to all agents during discussions.

### Supported File Types
- `.txt` - Plain text files
- `.md` - Markdown files
- `.csv` - CSV data files
- `.json` - JSON data files
- `.text` - Text files with .text extension

### How It Works

1. **Single File**: Pass a single text file to the discussion
   ```bash
   python run.py discuss "Summarize this document" --data ./report.txt
   ```

2. **Multiple Files**: Pass multiple files
   ```bash
   python run.py discuss "Compare these reports" --data ./report1.txt --data ./report2.md
   ```

3. **Directory**: Pass a directory and all supported text files will be loaded recursively
   ```bash
   python run.py discuss "What patterns do you see?" --data ./data_directory
   ```

4. **Mixed**: Combine files and directories
   ```bash
   python run.py discuss "Analyze all this data" --data ./file.txt --data ./folder
   ```

### Python API Usage

```python
from roundtable import Roundtable

# Initialize with data files
rt = Roundtable(
    max_rounds=3,
    data_files=['./data1.txt', './data_dir', './report.md']
)

# Agents will have access to all file contents
discussion = rt.discuss("What insights can you find in this data?")
```

### Benefits
- ✅ All agents see the same data
- ✅ Filenames and full content are provided
- ✅ Works with any text-based format
- ✅ Supports both individual files and entire directories
- ✅ Automatically handles file reading and formatting

---

## External Knowledge Tools 🔧

Three powerful research tools enhance roundtable discussions:

### 1. Tavily Web Search
- **Purpose**: Current information, recent news, up-to-date facts
- **Requires**: API key (free tier available)
- **Setup**: 
  ```
  TAVILY_API_KEY=your-api-key
  pip install tavily-python
  ```
- **Use Case**: Discussions about current events, latest technology, breaking news

### 2. Wikipedia
- **Purpose**: General knowledge, historical facts, biographical information
- **Requires**: None (free, pre-installed)
- **Setup**: 
  ```
  pip install wikipedia-api
  ```
- **Use Case**: Historical context, factual information, background knowledge

### 3. ArXiv Academic Papers
- **Purpose**: Research papers, scientific findings, academic references
- **Requires**: None (free, pre-installed)
- **Setup**: 
  ```
  pip install arxiv
  ```
- **Use Case**: Technical discussions, scientific research, academic topics

### Enable Tools

```bash
# Single discussion with tools
python run.py discuss "Quantum computing advances?" --tools

# Check configuration
python run.py tools-status
```

---

## 💻 Usage Examples

### Command Line Interface

### Advanced Options

```bash
# More rounds for deeper discussion
python run.py discuss "Future of remote work?" --rounds 5

# Adjust creativity (0.0=focused, 1.0=creative)
python run.py discuss "Creative problem-solving?" --temperature 0.9

# Export to file
python run.py discuss "What makes great leadership?" --export markdown -o discussion.md

# With data files
python run.py discuss "Analyze this data" --data ./data.txt --data ./reports_dir

# With all options
python run.py discuss "AI ethics?" --rounds 5 --tools --data ./research --export markdown -o output.md

# Quiet mode (minimal output)
python run.py discuss "Topic" --quiet --export json -o output.json

# Disable moderator
python run.py discuss "Topic" --no-moderator
```

### Check Configuration

```bash
# Show configured models
python run.py info

# Show available tools
python run.py tools-status

# Show example configuration
python run.py example
```

---

## 📺 Example Output

Here's what a typical discussion looks like:

```
🎯 Question: What's the meaning of life?

👥 Participants: 4
   • Participant 1: gpt-4o
   • Participant 2: claude-sonnet-4-20250514
   • Participant 3: meta-llama-3.3-70b-instruct
   • Participant 4: deepseek-ai/DeepSeek-R1-0528

================================================================================

🔄 Round 1/4
--------------------------------------------------------------------------------

💬 Participant 1 (gpt-4o):
The meaning of life is a deeply personal and subjective concept that can vary 
greatly among individuals. Many find meaning through relationships, personal 
growth, or contributing to something larger than themselves. Philosophically, 
it could be seen as a quest for purpose, exploring what it means to live a 
fulfilling and ethical life.

💬 Participant 2 (claude-sonnet-4-20250514):
I'd suggest that meaning in life emerges from the intersection of three elements: 
our capacity to form deep connections with others, our ability to contribute 
something of value that extends beyond ourselves, and our ongoing growth through 
learning and overcoming challenges. Rather than being a fixed destination, meaning 
seems to be something we actively create through our choices and relationships.

💬 Participant 3 (meta-llama-3.3-70b-instruct):
I believe the meaning of life is deeply personal yet often revolves around the 
pursuit of purpose, happiness, and fulfillment through cultivating meaningful 
relationships, contributing to something larger than oneself, and finding a sense 
of belonging. The pursuit of knowledge, personal growth, and self-actualization 
can also be a vital part of this journey.

💬 Participant 4 (deepseek-ai/DeepSeek-R1-0528):
My perspective draws from Viktor Frankl's logotherapy: The meaning of life isn't 
a single universal answer, but is uniquely discovered through our responses to 
life's challenges. It emerges through creating meaningful work, experiencing love, 
and adopting courage amid unavoidable suffering.

[... 3 more rounds of discussion ...]

================================================================================
📊 Generating Final Summary...

📋 Final Summary:
The roundtable discussion emphasized that meaning is a deeply personal yet 
relational concept - not a fixed destination but a dynamic process actively 
co-created through personal choices, relationships, and contributions. Key insights 
included the importance of narrative, mindfulness, and legacy in shaping meaning, 
with emphasis on how life's meaning emerges through the conscious weaving of 
personal authenticity into collective flourishing.

The discussion acknowledged that meaning-making is shaped by access, agency, and 
socioeconomic realities, underscoring a collective responsibility to foster 
environments where diverse individuals can explore their potential. Ultimately, 
the synthesis suggested that meaning thrives in the interplay of agency and 
impermanence, urging individuals to create significance amid uncertainty.

================================================================================
✓ DISCUSSION COMPLETE
================================================================================
```

---

## Project Structure

```
roundtable/
├── llm.py                    # LLM authentication
├── roundtable.py             # Core discussion engine
├── tools.py                  # External knowledge tools ⭐
├── cli.py                    # Command-line interface
├── run.py                    # Entry point
├── __init__.py               # Package initialization
├── requirements.txt          # Dependencies
├── env.template              # Configuration template
├── .gitignore               # Git ignore patterns
├── README.md                # This file
├── QUICKSTART.md            # Quick start guide
└── example.py               # API usage examples
```

## API Support

Works with any OpenAI-compatible API:
- ✅ OpenAI (GPT-4o, GPT-4, GPT-3.5)
- ✅ Anthropic Claude (via compatibility layer)
- ✅ Friendli AI (Llama, DeepSeek, Qwen)
- ✅ Local models (LM Studio, Ollama with OpenAI endpoint)
- ✅ Azure OpenAI
- ✅ Any other OpenAI-compatible service

## Use Cases

### Research & Analysis
```bash
# Gather diverse AI perspectives on complex topics
python run.py discuss "Implications of AGI development?" --tools --rounds 5
```

### Decision Making
```bash
# Get multiple viewpoints before making important decisions
python run.py discuss "Best strategy for scaling our business?" --tools
```

### Data Analysis
```bash
# Analyze text data, reports, or documents
python run.py discuss "What patterns exist in this data?" --data ./data_dir --rounds 4

# Compare multiple documents
python run.py discuss "How do these reports differ?" --data ./report1.txt --data ./report2.txt
```

### Brainstorming
```bash
# Generate ideas through collaborative discussion
python run.py discuss "Innovative products we could build?" --temperature 0.9
```

### Education
```bash
# Learn about topics from different AI perspectives
python run.py discuss "History of quantum mechanics?" --tools
```

### Red Teaming
```bash
# Identify weaknesses through multi-model analysis
python run.py discuss "Security vulnerabilities in our system?" --tools
```

---

## 🐍 Python API

### Programmatic Usage

Use Roundtable directly in your Python applications:

```python
from roundtable import Roundtable

# Initialize with tools
rt = Roundtable(
    max_rounds=3,
    temperature=0.7,
    tools_enabled=True  # Enable external tools
)

# Conduct discussion
discussion = rt.discuss("Your question here")

# Export
markdown = rt.export_discussion(discussion, format="markdown")
with open("output.md", "w") as f:
    f.write(markdown)
```

### With Data Files

```python
from roundtable import Roundtable

# Initialize with data files
rt = Roundtable(
    max_rounds=3,
    temperature=0.7,
    data_files=['./data.txt', './reports_dir', './analysis.md']
)

# Conduct discussion - agents will have access to all file contents
discussion = rt.discuss("What insights can you find in the provided data?")

# Access file information
print(f"Files loaded: {len(discussion.file_data)}")
for file in discussion.file_data:
    print(f"  - {file['filename']} ({file['size']} chars)")
```

### Custom Participant Configuration

```python
from roundtable.llm import get_llm_client

# Add custom participants
custom_llm = get_llm_client(
    model="custom-model",
    api_key="your-key",
    base_url="https://custom-api.com/v1",
    temperature=0.8
)
```

---

## 💡 Tips for Better Discussions

1. **Clear Questions**: Specific, well-defined questions get better responses
   - ✅ Good: "What are the main challenges in deploying AI in healthcare?"
   - ❌ Bad: "Tell me about AI"

2. **Multiple Rounds**: 3-5 rounds allow ideas to evolve and build
   - Round 1: Initial perspectives
   - Round 2-3: Building and refining
   - Round 4-5: Synthesis and conclusions

3. **Temperature Control**: Adjust creativity based on topic
   - 🔥 High (0.7-0.9): Creative brainstorming, innovative ideas
   - ❄️ Low (0.3-0.5): Analytical tasks, factual discussions

4. **Diverse Models**: Mix different model types for varied perspectives
   - Combine reasoning-focused (GPT-4) with creative (Claude) models
   - Include open-source models (Llama) for balanced viewpoints

5. **Moderator**: Enable for complex topics needing synthesis
   - Highly recommended for 4+ participants
   - Creates coherent summaries from diverse viewpoints

6. **Tools**: Use `--tools` for research-heavy topics
   - Current events → Tavily web search
   - Historical facts → Wikipedia
   - Academic topics → ArXiv

---

## 🔧 Troubleshooting

### Common Issues

#### "No participants configured"
```bash
# Solution: Configure at least one participant in .env
MODEL1=gpt-4o
API_KEY1=your-api-key
BASE_URL1=https://api.openai.com/v1
```

#### "API key not provided"
- ✅ Check `.env` file exists in the project directory
- ✅ Verify API keys are correctly formatted (no quotes needed)
- ✅ Ensure `.env` is in the same directory as `run.py`
- ✅ Check for typos in variable names (MODEL1, not Model1)

#### "Tools not available"
```bash
# Check which tools are configured
python run.py tools-status

# Install missing tool dependencies
pip install tavily-python wikipedia-api arxiv
```

#### Model Returns 404 Error
- ✅ Verify model name is correct for your provider
  - OpenAI: `gpt-4o`, `gpt-4`, `gpt-3.5-turbo`
  - Anthropic: `claude-sonnet-4-20250514`, `claude-opus-4-20250514`
  - Check provider docs for exact model names
- ✅ Ensure API key has access to the specified model
- ✅ Verify BASE_URL is correct for your provider

#### Models Not Responding / Timeout
- ✅ Check API keys are valid and active
- ✅ Verify BASE_URL matches your provider's endpoint
- ✅ Test connectivity: `python run.py info`
- ✅ Check API rate limits or quota
- ✅ Ensure firewall isn't blocking API requests

#### "ModuleNotFoundError"
```bash
# Reinstall dependencies
pip install -r requirements.txt

# Or install specific missing module
pip install langchain langchain-openai python-dotenv click rich
```

### Getting Help

- 📖 Check [QUICKSTART.md](QUICKSTART.md) for detailed setup
- 💬 Open an [issue on GitHub](https://github.com/mamipour/roundtable/issues)
- 🔍 Search [existing issues](https://github.com/mamipour/roundtable/issues?q=is%3Aissue)

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Ways to Contribute

- 🐛 **Report Bugs**: Open an issue describing the bug and steps to reproduce
- ✨ **Suggest Features**: Share ideas for new features or improvements
- 📝 **Improve Documentation**: Fix typos, clarify instructions, add examples
- 💻 **Submit Code**: Fork the repo and submit a pull request

### Development Setup

```bash
# Fork and clone the repository
git clone https://github.com/mamipour/roundtable.git
cd roundtable

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
python run_test.py

# Make your changes and test thoroughly
```

### Pull Request Guidelines

1. Create a new branch for your feature: `git checkout -b feature-name`
2. Make your changes and test thoroughly
3. Update documentation if needed
4. Commit with clear messages: `git commit -m "Add feature: description"`
5. Push and create a pull request

### Code Style

- Follow PEP 8 guidelines
- Add docstrings to functions and classes
- Keep functions focused and modular
- Comment complex logic

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

You are free to:
- ✅ Use commercially
- ✅ Modify
- ✅ Distribute
- ✅ Use privately

---

## 🙏 Credits & Acknowledgments

Built with powerful open-source tools:

- **[LangChain](https://python.langchain.com/)** - LLM orchestration framework
- **[Rich](https://rich.readthedocs.io/)** - Beautiful terminal formatting
- **[Click](https://click.palletsprojects.com/)** - Elegant CLI framework
- **[Tavily](https://tavily.com/)** - Web search API
- **[Wikipedia API](https://pypi.org/project/Wikipedia-API/)** - Knowledge base access
- **[arXiv](https://arxiv.org/)** - Academic paper search

Authentication system adapted from `tau_helper` project.

---

## ⭐ Star History

If you find Roundtable useful, please consider giving it a star on GitHub! ⭐

---

## 📞 Contact & Support

- 📧 **Issues**: [GitHub Issues](https://github.com/mamipour/roundtable/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/mamipour/roundtable/discussions)
- 🐦 **Twitter**: [@mamipour](https://twitter.com/mamipour)

---

## 🎯 Keywords

`multi-agent AI` `collaborative AI` `AI brainstorming` `LangChain` `GPT-4` `Claude` `Llama` `AI discussion` `roundtable` `AI orchestration` `multi-model AI` `AI collaboration` `LLM framework` `AI research tool` `decision making AI` `brainstorming tool`

---

<div align="center">

**Made with ❤️**

[⬆ Back to Top](#-roundtable-multi-agent-ai-brainstorming-system)

</div>

