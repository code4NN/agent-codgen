from dotenv import load_dotenv
load_dotenv()

from prompts._loader import load_prompt_parts
from llm.client import call_llm


def test_prompt_loader_and_gemini():
    # Example problem text (multi-line on purpose)
    problem_text = """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution.
    """

    # Load and render prompt
    system_prompt, user_prompt = load_prompt_parts(
        "parse_problem",
        variables={
            "problem_text": problem_text
        }
    )

    print("\n--- SYSTEM PROMPT ---\n")
    print(system_prompt)

    print("\n--- USER PROMPT ---\n")
    print(user_prompt)

    # Call Gemini
    response = call_llm(
        model="gemini-2.5-flash",
        system_prompt=system_prompt,
        prompt=user_prompt,
        temperature=0.0,
        max_tokens=5024,
    )

    print("\n--- GEMINI RESPONSE ---\n")
    print(response.text)


if __name__ == "__main__":
    test_prompt_loader_and_gemini()
