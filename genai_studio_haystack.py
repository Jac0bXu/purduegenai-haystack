from haystack import component
import requests

#---
provided_models = [
    # "deepseek-r1:1.5b"
    # "deepseek-r1:7b",
    # "deepseek-r1:14b"
    # "deepseek-r1:32b",
    # "deepseek-r1:70b",
    # "gemma:latest",  # 9b
    # "llama3.1:latest",
    # "llama3.1:70b-instruct-q4_K_M",
    # "llama3.2:latest"
    # "llama3.3:70b-instruct-q4_K_M",
    # "llava:latest",
    # "mistral:latest",
    # "phi4:latest",
    # "qwen2.5:72b",
    # "qwq:latest"
]

#---
@component
class GenAIStudioGenerator:
    """
    A Haystack component that calls the Purdue GenAI Studio API to generate a text response.
    """
    
    def __init__(self, api_key: str, system_prompt: str = "You are a helpful AI assistant.", model_name: str = "deepseek-r1:70b"):
        self.api_key = api_key
        self.system_prompt = system_prompt
        self.model_name = model_name
        self.url = "https://genai.rcac.purdue.edu/api/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
    
    @component.output_types(answer=str, note=str)
    def run(self, query: str) -> dict:
        payload = {
            "model": self.model_name,
            "messages": [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": query}
            ],
            "temperature": 0.2,
            "max_tokens": 2000,
            "stream": False
        }
        try:
            response = requests.post(self.url, headers=self.headers, json=payload)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            result = response.json()
            content = result["choices"][0]["message"]["content"]
            return {"answer": content, "note": "LLM call successful"}
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 500:
                return {"answer": "Failed to generate", "note": "Internal server error (500)"}
            else:
                raise Exception(f"Error: {response.status_code}, {response.text}")