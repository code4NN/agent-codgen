from typing import Any, Literal
from pydantic import BaseModel

class TestCase(BaseModel):
    inputs: Any
    expected: Any
    assertion_type: Literal["exact", "set", "predicate"]
    justification: str
