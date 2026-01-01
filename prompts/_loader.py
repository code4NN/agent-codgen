from pathlib import Path
from typing import Optional, Tuple, Dict, Any

PROMPT_DIR = Path(__file__).parent


def load_prompt_parts(
    name: str,
    variables: Optional[Dict[str, Any]] = None,
) -> Tuple[Optional[str], str]:
    """
    Load a prompt file, split into SYSTEM and USER sections,
    and perform simple variable substitution.

    Prompt format:

    [SYSTEM]
    ... multi-line text ...

    [USER]
    ... multi-line text with {{placeholders}} ...

    Rules:
    - Variables are replaced via {{key}} → str(value)
    - Missing variables raise an error
    - No logic, no templating, no conditionals
    """

    path = PROMPT_DIR / f"{name}.md"
    if not path.exists():
        raise FileNotFoundError(f"Prompt not found: {path}")

    text = path.read_text(encoding="utf-8")

    # --- Split roles ---
    system_prompt: Optional[str] = None
    user_prompt: Optional[str] = None

    if "[SYSTEM]" in text:
        text = text.split("[SYSTEM]", 1)[1]

    if "[USER]" in text:
        sys_part, user_part = text.split("[USER]", 1)
        system_prompt = sys_part.strip() or None
        user_prompt = user_part.strip()
    else:
        user_prompt = text.strip()

    if not user_prompt:
        raise ValueError(f"Prompt '{name}' has no USER content")

    # --- Variable substitution ---
    if variables:
        for key, value in variables.items():
            placeholder = f"{{{{{key}}}}}"
            replacement = str(value)
            if system_prompt:
                system_prompt = system_prompt.replace(placeholder, replacement)
            user_prompt = user_prompt.replace(placeholder, replacement)

        # Detect unreplaced placeholders (very important)
        unresolved = []
        for block in [system_prompt, user_prompt]:
            if block and "{{" in block and "}}" in block:
                unresolved.append(block)

        if unresolved:
            raise ValueError(
                f"Unresolved placeholders in prompt '{name}'. "
                f"Variables provided: {list(variables.keys())}"
            )

    return system_prompt, user_prompt
