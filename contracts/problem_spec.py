from typing import List, Literal
from pydantic import BaseModel

class Argument(BaseModel):
    name: str
    type: str

class Ambiguity(BaseModel):
    description: str
    options: List[str]
    default: str
    blocking: bool

class ProblemSpec(BaseModel):
    function_name: str
    inputs: List[Argument]
    output_type: str
    input_mode: Literal["positional", "keyword"]
    multiple_valid_outputs: bool
    edge_cases: List[str]
    ambiguities: List[Ambiguity]
    confidence: float
