from abc import ABC, abstractmethod
from llm.types import LLMRequest, LLMResponse

class BaseLLMClient(ABC):
    """
    Abstract base class for all LLM clients.
    """

    @abstractmethod
    def generate(self, request: LLMRequest) -> LLMResponse:
        pass
