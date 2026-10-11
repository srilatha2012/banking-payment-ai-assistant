def build_prompt(
    payment_type: str,
    issue: str,
    reference: str,
) -> str:
    return f"""
Payment type: {payment_type}

Reference:
{reference}

User's question or issue:
{issue}

Start directly with these exact Markdown headings.
Put each heading on its own line, with a blank line before
and after it:

### 1. What is known

### 2. Possible causes

### 3. What to check next

### 4. What is unknown

Rules:
- Use only the supplied reference for factual explanations.
- In "What is known", copy the supplied reference exactly.
- Treat the input as a knowledge lookup or hypothetical scenario.
  It does not confirm the state of an actual transaction.
- Do not assume the account belongs to the user.
- Do not invent transaction details or unsupported causes.
- If the reference gives no underlying causes, write:
  "The specific underlying cause is unknown from the reference."
- In "What to check next", begin the check with the exact
  words "Suggested check:".
- For ACH, suggest verifying the exact return code in the bank
  or processor's return record, if available to an authorized reviewer.
- For Wire, suggest verifying the exact status and its meaning
  with the sending bank, if available to an authorized reviewer.
- Do not promise completion, recommend automatic resubmission,
  or invent processing deadlines.
- In "What is unknown", identify missing transaction details.
  No actual transaction details have been provided for this lookup.
- For ACH, state that no transaction amount, processing date,
  or account balance was provided.
- Preserve "and/or" when explaining ACH balances.
- Do not repeat the underlying-cause sentence in the checks section.
- Keep the answer concise.
- If the reference lists possible delay factors, summarize them
  in "Possible causes" and state that none is confirmed for
  a particular transaction.
- If the reference lists possible delay factors, summarize them
  in "Possible causes" and state that none is confirmed for
  a particular transaction.
- For Wire, state that the actual status, sending date,
  banks involved, and expected arrival date were not provided.
  Do not mention account balance unless relevant to the reference.00000+++++++++++++++++
""".strip()