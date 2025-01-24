# Gemini multimodal API calls

This is a simple demo repo that shows how to make multimodal API calls to Gemini 2.0 Flash with LiteLLM. (I found the LiteLLM documentation on this inadequate.) The code should work with any kind of media, including images, videos, audio, and PDFs. You only need to change the `media_path` and `prompt` in the `main.py` file to fit your use case.

## Prerequisites

This demo repo uses the the `uv` package manager to manage dependencies. If you don't already have `uv` installed, you can install it with the following curl command:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

You will also need Python, which you can install with:

```bash
uv python install
```

## Setup

1. Clone the repo with `git clone https://github.com/chriscarrollsmith/gemini-multimodal-api-calls.git`
2. Navigate into the folder with `cd gemini-multimodal-api-calls`
3. Create a `.env` file with the `GEMINI_API_KEY` environment variable
4. Install the dependencies with `uv sync`
5. Run the `main.py` file

## Example

### Prompt

```python
prompt = 'Can you tell me the name of this meme template?'
```

### Image

[![](./meme.jpg)](./meme.jpg)

### Output

"The meme template you're asking about is called **"Anime Running Away from Kid"**. It's sometimes also referred to as **"Anime Girl Running Away From Boy"**."
