from ollama import chat

reference = """
Nacha reference: R01 means Insufficient Funds.
The available balance and/or cash reserve balance is not sufficient
to cover the dollar value of the ACH debit entry.
"""

response = chat(
    model="gemma3:4b",
    messages=[
        {
            "role": "system",
            "content": (
                "You are an ACH payment operations assistant. "
                "Use only the supplied reference for confirmed facts. "
                "Do not assume who the user is or what account records they can access. "
                "If the reference does not establish a detail, say it is unknown."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Reference:\n{reference}\n\n"
                "An ACH debit was returned with R01. "
                "Explain what is confirmed and what is still unknown."
            ),
        },
    ],
)

print(response.message.content)