from llm.base import BaseLLMClient
from llm.types import LLMRequest, LLMResponse

class OpenAIClient(BaseLLMClient):
    def __init__(self, model: str):
        self.model = model

    def generate(self, request: LLMRequest) -> LLMResponse:
        raise NotImplementedError("OpenAI client not wired yet")
