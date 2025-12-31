from llm.base import BaseLLMClient
from llm.types import LLMRequest, LLMResponse

class GeminiClient(BaseLLMClient):
    def __init__(self, model: str):
        self.model = model

    def generate(self, request: LLMRequest) -> LLMResponse:
        raise NotImplementedError("Gemini client not wired yet")
