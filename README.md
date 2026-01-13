# LLM Embodiment - Prisoner's Dilemma

Runs the Prisoner's Dilemma game against an LLM with different system prompts to measure behavioral variation.

## Setup

```bash
pip install -r requirements.txt
```

Requires an Ollama server running with the target model.

## Usage

Edit `run_system_prompts.py` to configure:
- `MODEL` - Ollama model name
- `HOST` / `PORT` - Ollama server address
- `N` - iterations per prompt

Run:
```bash
python -u run_system_prompts.py
```

## Files

- `all_prompts.json` - Input system prompts (283 prompts)
- `run_system_prompts.py` - Main script
- `requirements.txt` - Dependencies

## Output

Generates `prisoners_dilemma_notes_<timestamp>.csv` with columns:
- `choice` - "Stay Silent" or "Confess"
- `note` - LLM's reasoning
- `prompt` - System prompt used
- `model` - Model name
