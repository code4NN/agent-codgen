from pathlib import Path
from typing import Dict, Optional

PROMPT_DIR = Path(__file__).parent

def load_prompt(name: str) -> str:
    """
    Load a prompt template by filename (without extension).
    Example: load_prompt("parse_problem")
    """
    path = PROMPT_DIR / f"{name}.md"
    if not path.exists():
        raise FileNotFoundError(f"Prompt not found: {path}")
    return path.read_text(encoding="utf-8")

def render_prompt(template: str, variables: Optional[Dict[str, str]] = None) -> str:
    """
    Minimal variable substitution.
    Uses {{var}} placeholders.
    """
    if not variables:
        return template

    for key, value in variables.items():
        template = template.replace(f"{{{{{key}}}}}", str(value))

    return template
