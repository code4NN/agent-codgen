from typing import Optional, Dict
from pydantic import BaseModel

class LLMRequest(BaseModel):
    prompt: str
    temperature: float = 0.0
    max_tokens: int = 512
    
    system_prompt: Optional[str] = None
    top_p: Optional[float] = None

class LLMResponse(BaseModel):
    text: str
    raw: Dict
