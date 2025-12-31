from typing import Optional, Dict
from pydantic import BaseModel

class LLMRequest(BaseModel):
    prompt: str
    system_prompt: Optional[str] = None
    temperature: float = 0.0
    max_tokens: int = 512

class LLMResponse(BaseModel):
    text: str
    raw: Dict
