from llm.openai_client import OpenAIClient
from llm.gemini_client import GeminiClient

def get_llm_client(model: str):
    if model.startswith("gpt"):
        return OpenAIClient(model)
    if model.startswith("gemini"):
        return GeminiClient(model)
    
    raise ValueError(f"Unknown model: {model}")
