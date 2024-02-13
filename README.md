# Overview

| Developed by | Guardrails AI |
| Date of development | Feb 15, 2024 |
| Validator type | Format |
| Blog |  |
| License | Apache 2 |
| Input/Output | Output |

# Description

This validator ensures that a generated output responds to the prompt given.

# Installation

```bash
$ guardrails hub install hub://guardrails/responsiveness_check
```

# Usage Examples

## Validating string output via Python

In this example, we’ll test that a generated output actually answers the question posed in the prompt.

```python
# Import Guard and Validator
from guardrails.hub import ResponsivenessCheck
from guardrails import Guard

prompt = "What is the capital of Missouri?"

# Setup Guard
guard = Guard.use(ResponsivenessCheck, prompt)

guard.validate("Jefferson City is the capital of Missouri.")  # Validation passes
guard.validate("Paris is the capital of France.")  # Validation fails because this response isn't related to what we asked.
```

# API Reference

`__init__`
- `prompt`: The original prompt to the LLM.
- `llm_callable`: Model name to make the litellm call.  Defaults to `gpt-3.5-turbo`.
- `on_fail`: The policy to enact when a validator fails.  Defaults to `noop`
