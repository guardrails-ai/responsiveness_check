import os
import pytest
from guardrails import Guard
from validator import ResponsivenessCheck

prompt = "What is the capital of Missouri?"
guard = Guard.from_string(validators=[ResponsivenessCheck(prompt=prompt, on_fail="exception")])

@pytest.mark.skipif(
    os.environ.get("OPENAI_API_KEY") in [None, "mocked"],
    reason="openai api key not set",
)
def test_pass():
  test_output = "Jefferson City is the capital of Missouri."
  result = guard.parse(test_output)
  
  assert result.validation_passed is True
  assert result.validated_output == test_output


@pytest.mark.skipif(
    os.environ.get("OPENAI_API_KEY") in [None, "mocked"],
    reason="openai api key not set",
)
def test_fail_non_responsive():
  with pytest.raises(Exception) as excinfo:
    test_output = "Paris is the capital of France."
    guard.parse(test_output)
  
  # Sometimes this test will fail bc the llm is unsure.
  assert str(excinfo.value) == "Validation failed for field with errors: The LLM says 'No'. The validation failed."


# TODO: Is this behaviour expected?
@pytest.mark.skipif(
    os.environ.get("OPENAI_API_KEY") in [None, "mocked"],
    reason="openai api key not set",
)
def test_fail_responsive_but_incorrect():
  with pytest.raises(Exception) as excinfo:
    test_output = "Kansas City is the capital of Missouri."
    guard.parse(test_output)
  
  assert str(excinfo.value) == "Validation failed for field with errors: The LLM says 'No'. The validation failed."
