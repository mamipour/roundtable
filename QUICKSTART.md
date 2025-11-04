# Roundtable Quick Start

## 1. Install Dependencies

```bash
cd roundtable
pip install -r requirements.txt
```

## 2. Configure API Keys

```bash
# Copy template
cp env.template .env

# Edit .env with your API keys (at minimum, set MODEL1 and API_KEY1)
```

**Minimum Configuration:**

```env
MODEL1=gpt-4o
API_KEY1=your-openai-api-key
BASE_URL1=https://api.openai.com/v1
```

**Full Multi-Agent Configuration:**

```env
# Participant 1: GPT-4o
MODEL1=gpt-4o
API_KEY1=your-openai-key
BASE_URL1=https://api.openai.com/v1

# Participant 2: Claude
MODEL2=claude-sonnet-4.5
API_KEY2=your-anthropic-key
BASE_URL2=https://api.anthropic.com/v1

# Participant 3: Llama
MODEL3=meta-llama/Llama-3.3-70B-Instruct
API_KEY3=your-friendli-key
BASE_URL3=https://api.friendli.ai/serverless/v1

# Moderator (optional)
MODERATOR_MODEL=gpt-4o
MODERATOR_API_KEY=your-openai-key
```

## 3. Run Your First Discussion

```bash
python run.py discuss "What are the key challenges in AI safety?"
```

## 4. Try Different Options

```bash
# More rounds for deeper discussion
python run.py discuss "Future of remote work?" --rounds 5

# Export to markdown
python run.py discuss "What makes great leadership?" --export markdown -o discussion.md

# Adjust creativity
python run.py discuss "Creative writing tips?" --temperature 0.9

# With data files (analyze text files)
python run.py discuss "What insights do you see?" --data ./my_data.txt

# With a directory of files
python run.py discuss "Analyze all these reports" --data ./reports_directory

# Check configuration
python run.py info
```

## 5. Using Data Files

Roundtable can analyze text files and directories:

```bash
# Create a sample text file
echo "AI is transforming industries worldwide." > sample.txt

# Discuss with the file
python run.py discuss "Summarize the key points" --data sample.txt

# Multiple files
python run.py discuss "Compare these documents" --data file1.txt --data file2.txt

# Entire directory
python run.py discuss "What patterns exist?" --data ./data_folder
```

**Supported file types:** `.txt`, `.md`, `.csv`, `.json`, `.text`

All agents will have access to both filenames and full content of the files.

## Example Output

```
🎯 Question: What are the key challenges in AI safety?

👥 Participants: 3
   • Participant 1: gpt-4o
   • Participant 2: claude-sonnet-4.5
   • Participant 3: meta-llama/Llama-3.3-70B-Instruct

================================================================================

🔄 Round 1/3
--------------------------------------------------------------------------------

💬 Participant 1 (gpt-4o):
The primary challenges include alignment (ensuring AI goals match human values),
interpretability (understanding AI decisions), and control (preventing unintended
consequences as systems grow more capable).

💬 Participant 2 (claude-sonnet-4.5):
Building on the alignment point, I'd emphasize the difficulty of specifying
human values precisely. We need robust feedback mechanisms and the challenge
of reward hacking in reinforcement learning systems.

💬 Participant 3 (meta-llama/Llama-3.3-70B-Instruct):
Adding to these concerns, scalability of oversight is critical. As AI systems
become more powerful, our ability to monitor and verify their behavior must
scale accordingly. This includes both technical and governance challenges.

[... more rounds ...]

📋 Final Summary:
This roundtable identified three interconnected pillars of AI safety:

1. **Value Alignment**: Ensuring AI systems pursue goals aligned with human
   values, complicated by the difficulty of precisely specifying those values

2. **Interpretability & Control**: Making AI decision-making transparent while
   preventing unintended consequences and reward hacking

3. **Scalable Oversight**: Developing monitoring and governance frameworks that
   can keep pace with rapidly advancing AI capabilities

The discussion emphasized that these challenges require coordinated efforts
across technical research, policy development, and international cooperation.
```

## Tips

- **Clear Questions**: Specific questions get better responses
- **3-5 Rounds**: Optimal for most topics (balance depth vs time)
- **Temperature**: 0.7 (balanced), 0.3 (focused), 0.9 (creative)
- **Multiple Models**: Different models bring different perspectives
- **Export**: Save interesting discussions for later reference

## Troubleshooting

**"No participants configured"**
```bash
# Check .env exists
ls -la .env

# Verify MODEL1 and API_KEY1 are set
cat .env | grep MODEL1
```

**"API key not provided"**
```bash
# Make sure .env is in the roundtable directory
pwd  # Should show /path/to/roundtable
ls .env
```

**Test configuration:**
```bash
python run.py info
```

## Next Steps

- See `README.md` for full documentation
- Try `python run.py --help` for all commands
- Explore advanced options with `python run.py discuss --help`

