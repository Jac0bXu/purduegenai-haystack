import os
from haystack import Pipeline
from haystack.components.builders import PromptBuilder
from genai_studio_haystack import GenAIStudioGenerator

API_KEY = os.getenv("GENAI_API_KEY")

LLM_pipeline = Pipeline()
LLM_pipeline.add_component("prompt_builder", PromptBuilder(template="You are a helpful AI assistant. {query}"))
LLM_pipeline.add_component("llm", GenAIStudioGenerator(api_key=API_KEY))
LLM_pipeline.connect("prompt_builder", "llm")

result = LLM_pipeline.run({"prompt_builder": {"query": "What is the capital of France?"}})
print(result)   
print(result["llm"]["answer"])

