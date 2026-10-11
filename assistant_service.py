from references import references, wire_references
from prompts import build_prompt
from llm_service import ask_model


def get_answer(return_code: str) -> str:
    return_code = return_code.strip().upper()

    if not return_code:
        return "Please enter an ACH return code."

    if len(return_code) > 20:
        return "Please enter an ACH return code of 20 characters or fewer."

    reference = references.get(return_code)

    if reference is None:
        return f"""
### 1. What is known

You entered code {return_code}.

### 2. Possible causes

Cannot determine from the available reference.

### 3. What to check next

Suggested check: verify the exact return code in the bank
or processor's return record, if available to an authorized reviewer.

### 4. What is unknown

Our reference data does not cover {return_code}.
Its meaning cannot be confirmed.
""".strip()

    prompt = build_prompt(
        payment_type="ACH",
        issue=(
            f"Explain ACH return code {return_code} "
            "using the supplied reference. "
            "No actual transaction details have been provided."
        ),
        reference=reference,
    )

    return ask_model(prompt)


def get_wire_answer(topic: str) -> str:
    topic = topic.strip().upper()

    if not topic:
        return "Please select a Wire topic."

    reference = wire_references.get(topic)

    if reference is None:
        return (
            "This Wire topic is not covered by the available reference. "
            "Its meaning or cause cannot be confirmed."
        )

    prompt = build_prompt(
        payment_type="Wire",
        issue=(
            f"Explain the topic: {topic}. "
            "Use only the supplied reference. "
            "Present delay factors as possibilities, "
            "not confirmed causes of an actual payment delay. "
            "No actual transaction details have been provided."
        ),
        reference=reference,
    )

    return ask_model(prompt)