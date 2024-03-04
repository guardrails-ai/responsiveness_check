## Overview

| Developed by | Guardrails AI |
| --- | --- |
| Date of development | Feb 15, 2024 |
| Validator type | Format |
| Blog | - |
| License | Apache 2 |
| Input/Output | Output |

## Description

This validator ensures that a generated output responds to the given prompt.

## Installation

```bash
guardrails hub install hub://guardrails/responsiveness_check
```

## Usage Examples

### Validating string output via Python

In this example, we’ll test that a generated output actually answers the question posed in the prompt.

```python
# Import Guard and Validator
from guardrails.hub import ResponsivenessCheck
from guardrails import Guard

prompt = "What is the capital of Missouri?"

# Setup Guard
guard = Guard().use(ResponsivenessCheck, prompt=prompt, llm_callable="gpt-3.5-turbo")

guard.validate("Jefferson City is the capital of Missouri.", metadata={"pass_on_invalid": True})  # Validation passes
try:
    guard.validate("Paris is the capital of France.")  # Validation fails because this response isn't related to what we asked.
except Exception as e:
    print(e)
```

## API Reference

**`__init__(self, prompt, llm_callable='gpt-3.5-turbo', on_fail="noop")`**
<ul>

Initializes a new instance of the Validator class.

**Parameters:**

- **`prompt`** *(str):* The original prompt to the LLM.
- **`llm_callable`** *(str):* Model name to make the LiteLLM call. Defaults to `gpt-3.5-turbo`.
- **`on_fail`** *(str, Callable):* The policy to enact when a validator fails. If `str`, must be one of `reask`, `fix`, `filter`, `refrain`, `noop`, `exception` or `fix_reask`. Otherwise, must be a function that is called when the validator fails.

</ul>

<br>

**`__call__(self, value, metadata={}) → ValidationResult`**

<ul>

Validates the given `value` using the rules defined in this validator, relying on the `metadata` provided to customize the validation process. This method is automatically invoked by `guard.parse(...)`, ensuring the validation logic is applied to the input data.

Note:

1. This method should not be called directly by the user. Instead, invoke `guard.parse(...)` where this method will be called internally for each associated Validator.
2. When invoking `guard.parse(...)`, ensure to pass the appropriate `metadata` dictionary that includes keys and values required by this validator. If `guard` is associated with multiple validators, combine all necessary metadata into a single dictionary.

**Parameters:**

- **`value`** *(Any):* The input value to validate.
- **`metadata`** *(dict):* A dictionary containing metadata required for validation. Keys and values must match the expectations of this validator.
    
    
    | Key | Type | Description | Default | Required |
    | --- | --- | --- | --- | --- |
    | `pass_on_invalid` | Boolean | Whether to pass the validation if the LLM returns an invalid response | False | No |

</ul>
