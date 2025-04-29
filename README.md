# purduegenai-haystack

A custom Haystack component for calling the Purdue GenAI Studio API as a language model (LLM) in your pipelines.

## Features

- Wraps the Purdue GenAI Studio REST API in a Haystack component  
- Configurable model, system prompt, temperature, max tokens, streaming  
- Graceful handling of HTTP errors  

## Contents

- `genai_studio_haystack.py` – Defines the `GenAIStudioGenerator` component  
- `demo/demo.py` – Example showing how to wire up the component in a Haystack `Pipeline`  
- `LICENSE`  
- `.gitignore`

## Installation

```bash
git clone https://github.com/yourusername/purduegenai-haystack.git
cd purduegenai-haystack
pip install farm-haystack requests
```

Export your Purdue GenAI Studio API key:

```bash
export GENAI_API_KEY="your_purdue_genai_api_key"
```

## Usage

```python
from haystack import Pipeline
from haystack.components import PromptBuilder
from genai_studio_haystack import GenAIStudioGenerator
import os

pipe = Pipeline()
pipe.add_component("prompt_builder", PromptBuilder(template="You are a helpful AI. {query}"))
pipe.add_component("llm", GenAIStudioGenerator(api_key=os.getenv("GENAI_API_KEY")))
pipe.connect("prompt_builder", "llm")

result = pipe.run({"prompt_builder": {"query": "What is the capital of France?"}})
print(result["llm"]["answer"])
```

See `demo/demo.py` for a full example.

## Configuration

- `api_key` (str): Purdue GenAI Studio API key  
- `system_prompt` (str): Initial system message (default: `"You are a helpful AI assistant."`)  
- `model_name` (str): Model identifier (e.g., `"deepseek-r1:70b"`)  
- `temperature` (float), `max_tokens` (int), `stream` (bool)

Pass these to `GenAIStudioGenerator(...)` in your code.

## Demo

Run the demo script:

```bash
python demo/demo.py
```

## License

Released under the MIT License. See `LICENSE` for details.
