from llm.gemini_client import GeminiClient

def get_llm_client(model: str):
    if model.startswith("gemini"):
        return GeminiClient(model)
    
    raise ValueError(f"Unsupported model: {model}")
