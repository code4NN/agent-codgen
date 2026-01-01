from llm.base import BaseLLMClient
from llm.types import LLMRequest, LLMResponse

from google import genai
from google.genai import types


class GeminiClient(BaseLLMClient):
    def __init__(self, model: str):
        self.model_name = model
        self.client = genai.Client()

    def generate(self, request: LLMRequest) -> LLMResponse:
        try:
            config = types.GenerateContentConfig(
                system_instruction=request.system_prompt,
                temperature=request.temperature,
                max_output_tokens=request.max_tokens,
            )

            # top_p is optional and generic
            if request.top_p is not None:
                config.top_p = request.top_p

            response = self.client.models.generate_content(
                model=self.model_name,
                contents=[
                    types.Content(
                        role="user",
                        parts=[types.Part(text=request.prompt)]
                    )
                ],
                config=config,
            )

            # Detect MAX_TOKENS early and explicitly
            if (
                response.candidates
                and response.candidates[0].finish_reason
                and response.candidates[0].finish_reason.name == "MAX_TOKENS"
            ):
                raise RuntimeError(
                    "Gemini hit MAX_TOKENS before emitting text. "
                    "Increase max_tokens or simplify prompt."
                )

            text = self._extract_text(response)

            return LLMResponse(
                text=text,
                raw=response.model_dump(),
            )

        except Exception as e:
            raise RuntimeError(f"Gemini generation failed: {e}")

    @staticmethod
    def _extract_text(response) -> str:
        """
        Robust Gemini text extraction.
        Handles all known response shapes.
        """

        # 1️⃣ Best case: SDK convenience field
        if getattr(response, "text", None):
            return response.text

        # 2️⃣ Candidate content parts
        if response.candidates:
            candidate = response.candidates[0]

            content = getattr(candidate, "content", None)
            parts = getattr(content, "parts", None)

            if parts:
                for part in parts:
                    if getattr(part, "text", None):
                        return part.text

            # 3️⃣ Fallback (SDK-dependent)
            if getattr(candidate, "output_text", None):
                return candidate.output_text

        raise ValueError(
            "Gemini response contained no extractable text. "
            "Check raw response for diagnostics."
        )
