from typing import Literal
from pydantic import BaseModel

class Action(BaseModel):
    intent: Literal[
        "parse_problem",
        "clarify_problem",
        "generate_tests",
        "generate_code",
        "execute_code",
        "debug",
        "abstain"
    ]
    hypothesis: str
    tool: str
    rationale: str
