from llm.registry import get_llm_client
from llm.types import LLMRequest

def call_llm(model: str, **kwargs):
    client = get_llm_client(model)
    request = LLMRequest(**kwargs)
    return client.generate(request)
