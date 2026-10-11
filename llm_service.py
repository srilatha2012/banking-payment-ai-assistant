import logging

from httpx import TimeoutException
from ollama import Client, ResponseError


logger = logging.getLogger(__name__)

MODEL_NAME = "gemma3:4b"
#MODEL_NAME = "missing-test-model"

client = Client(
    host="http://localhost:11434",
    timeout=120.0,
    #timeout=0.001,
)


def ask_model(prompt: str) -> str:
    try:
        response = client.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": (
                       "You are an ACH and wire payment operations assistant. "
                       "Use only the supplied reference for factual "
                       "explanations of payment codes, statuses, and concepts. "
                        "Do not invent transaction details or unsupported causes. "
                        "Do not assume the account belongs to the user "
                        "or that the user can access account records. "
                        "Clearly state when information is unknown. "
                        "If a code is not covered by the reference, "
                        "say its meaning cannot be confirmed from the reference."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
        )

        answer = (response.message.content or "").strip()
        #answer = ""  # Temporary test

        if not answer:
            return (
                "The model returned an empty response. "
                "Please try again."
            )

        return answer

    except ConnectionError:
        return (
            "Cannot connect to Ollama. "
            "Please open the Ollama application and try again."
        )

    except TimeoutException:
        return (
            "The model took too long to respond. "
            "Please try again. The first request may take longer "
            "while the model loads."
        )

    except ResponseError as error:
        logger.exception("Ollama returned an error")

        if error.status_code == 404:
            return (
                f"The model '{MODEL_NAME}' could not be found. "
                f"Run `ollama pull {MODEL_NAME}` in your terminal, "
                "then try again."
            )

        return (
            "Ollama could not complete the request. "
            "Please try again. If the problem continues, "
            "check the terminal for details."
        )

    except Exception:
        logger.exception("Unexpected error while requesting an answer")

        return (
            "An unexpected error occurred while preparing the answer. "
            "Please check the terminal for details."
        )