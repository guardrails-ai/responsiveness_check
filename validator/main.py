from typing import Any, Callable, Dict, Optional

from guardrails.validator_base import (
    ValidationResult,
    register_validator,
)

from guardrails.hub.guardrails.response_evaluator.validator import ResponseEvaluator


@register_validator(name="guardrails/responsiveness_check", data_type="string")
class ResponsivenessCheck(ResponseEvaluator):  # type: ignore
    """Validates that a generated output responds to the prompt given.

    **Key Properties**

    | Property                      | Description                       |
    | ----------------------------- | --------------------------------- |
    | Name for `format` attribute   | `guardrails/responsiveness_check` |
    | Supported data types          | `string`                          |
    | Programmatic fix              | None                              |

    Args:
        prompt (string): The original prompt to the LLM.
        llm_callable (str, optional): Model name to make the litellm call.
            Defaults to `gpt-3.5-turbo`
        on_fail (Callable, optional): A function to call when validation fails.
            Defaults to None.
    """  # noqa

    def __init__(
        self,
        prompt: str,
        llm_callable: Optional[str] = "gpt-3.5-turbo",
        on_fail: Optional[Callable] = None,
    ):
        super().__init__(on_fail=on_fail, prompt=prompt, llm_callable=llm_callable)
        self._prompt = prompt

    def validate(self, value: Any, metadata: Dict) -> ValidationResult:
        metadata["validation_question"] = f"""Does this LLM Response respond to the following prompt?
        Prompt:
        {self._prompt}
        """

        return super().validate(value, metadata)
