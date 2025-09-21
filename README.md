# Gradio Client for Qwen/Qwen3-Coder-WebDev

This project provides example scripts to interact with the Qwen/Qwen3-Coder-WebDev Gradio app using the gradio_client library.

## Installation

1. Install Python if not already installed.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the examples:

```bash
python examples.py
```

Or import and use specific functions:

```python
from examples import generate_code_example

generate_code_example("Your input here", "System prompt")
```

## API Endpoints

The following API endpoints are available:

- `/lambda` to `/lambda_5`: Various lambda functions.
- `/generate_code`: Generate code based on input and system prompt.
- Modal operations: `/open_modal`, `/close_modal`, etc.
- System prompt management: `/update_system_prompt`, `/reset_system_prompt`
- History: `/clear_history`, `/render_history`

Refer to the examples.py file for usage of each endpoint.

## Web App

A Gradio web interface is provided in `app.py` for easy interaction.

Run locally:

```bash
python app.py
```

For a public URL, deploy to Hugging Face Spaces:

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces).
2. Create a new Space.
3. Select "Gradio" as the SDK.
4. Upload `app.py` and `requirements.txt`.
5. Your Space will have a public URL like `https://yourusername/yourspace.hf.space`.

## Enabling Grok Code Fast 1 (Preview)

The Grok Code Fast 1 (Preview) is enabled via the installed VS Code extension "sixth.sixth-ai".