import together

from typing import Any, Dict
from langchain.llms.base import LLM
from langchain.utils import get_from_dict_or_env


class TogetherLLM(LLM):
    """Together large language models."""

    model: str = "togethercomputer/llama-2-70b-chat"
    """model endpoint to use"""

    api_key: str = ""
    """Together API key"""

    temperature: float = 0.7
    """What sampling temperature to use."""

    max_tokens: int = 100
    """The maximum number of tokens to generate in the completion."""

    class Config:
        extra = "forbid"

    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that the API key is set."""
        api_key = get_from_dict_or_env(
            values, "together_api_key", "TOGETHER_API_KEY"
        )
        values["together_api_key"] = api_key
        return values

    @property
    def _llm_type(self) -> str:
        """Return type of LLM."""
        return "together"

    def _call(
            self,
            prompt: str,
            **kwargs: Any,
    ) -> str:
        """Call to Together endpoint."""
        together.api_key = self.api_key
        output = together.Complete.create(prompt,
                                          model=self.model,
                                          max_tokens=self.max_tokens,
                                          temperature=self.temperature,
                                          )
        text = output['output']['choices'][0]['text']
        return text
