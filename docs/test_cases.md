# MVP Test Cases

## Test Environment

- Test date: October 11, 2026
- Operating system: Windows
- UI: Streamlit
- Model runner: Ollama
- Model: gemma3:4b
- Normal request timeout setting: 120 seconds
- Methods: manual browser tests and a direct Python function check

## Current Scope

The MVP supports ACH return codes R01, R02, R03, and R04,
plus one Wire topic: international wire delays.

Supported inputs use stored local reference text in the model prompt.
The app does not retrieve websites during requests and does not
currently implement embeddings, a vector database, or semantic retrieval.

Unknown ACH codes receive a predefined response without a model call.

## Functional and Validation Tests

| ID | Test | Expected behavior | Observed result | Status |
|---|---|---|---|---|
| F01 | ACH: R01 | Display a structured answer using the stored R01 reference | Four sections displayed; definition matched the reference | Passed |
| F02 | ACH: R02 | Use the stored R02 reference without inventing a closure reason | Definition matched the reference; underlying cause stated as unknown | Passed |
| F03 | ACH: R03 | Use the stored R03 reference | Definition matched the displayed reference | Passed |
| F04 | ACH: R04 | Use the stored R04 reference | Definition matched the displayed reference | Passed |
| F05 | Wire: international wire delays | Present reference delay factors as possibilities, not confirmed transaction causes | Structured answer displayed with possible factors and uncertainty | Passed |
| V01 | ACH: XYZ123 | State that the code is not covered without inventing a definition | Meaning could not be confirmed | Passed |
| V02 | Empty ACH input | Display a validation warning | "Please enter an ACH return code." displayed | Passed |
| V03 | ACH: lowercase r01 | Normalize input and use the R01 reference | R01 answer displayed | Passed |
| V04 | Paste more than 20 characters into the ACH field | Limit UI input to 20 characters | Field displayed 20/20 characters | Passed |
| V05 | Call get_answer with 21 characters | Reject the input before a model call | Length-limit message printed in the terminal | Passed |

## Error Handling and Recovery Tests

| ID | Test method | Expected behavior | Observed result | Status |
|---|---|---|---|---|
| E01 | Temporarily set the model name to missing-test-model | Display a model-not-found message | Expected message displayed without a UI traceback | Passed |
| E02 | Restore gemma3:4b after E01 | Resume normal responses | R01 worked again | Passed |
| E03 | Quit Ollama and submit R01 | Display a connection-error message | "Cannot connect to Ollama." message displayed | Passed |
| E04 | Reopen Ollama after E03 | Resume normal responses | R01 worked again | Passed |
| E05 | Temporarily set timeout to 0.001 seconds | Display a timeout message | "The model took too long to respond." message displayed | Passed |
| E06 | Restore timeout to 120.0 after E05 | Resume normal responses | R01 worked again | Passed |
| E07 | Temporarily set the processed answer to an empty string | Display the empty-response fallback | "The model returned an empty response. Please try again." displayed | Passed |
| E08 | Restore response extraction after E07 | Resume normal responses | R01 worked again | Passed |
| E09 | Unexpected exception | Display a friendly message and log details | Handler reviewed in code; simulation skipped for MVP | Not tested |
| E10 | Ollama ResponseError other than 404 | Display a friendly message and log details | Handler reviewed in code; no failure simulated | Not tested |

E07 simulated an empty processed answer. It did not reproduce
an actual empty response from Ollama.

## UI and Reference Checks

| ID | Check | Observed result | Status |
|---|---|---|---|
| U01 | Required response headings | All four headings appeared in reviewed successful responses | Passed |
| U02 | ACH reference panel | Stored reference text, source link, and local-text explanation displayed | Passed |
| U03 | Wire reference panel | Source-display code reviewed; expanded panel not verified in the supplied screenshots | Not tested |
| U04 | Educational and privacy notice | Notice appeared below the app description | Passed |
| U05 | Application restart | ACH and Wire responses worked after restarting the application | Passed |

## Manual Output Review

The reviewed responses:

- Used the stored reference for factual explanations.
- Matched the displayed ACH reference in "What is known."
- Avoided inventing transaction amounts, dates, or account balances.
- Stated when the underlying cause was unknown.
- Labeled investigation guidance with "Suggested check:".
- Presented Wire delay factors as possibilities.

These observations apply to the tested outputs. They do not
guarantee that every future model response will follow the prompt.

## Direct Service Length Check

Run from the project folder in PowerShell:

    .\.venv\Scripts\python.exe -c "from assistant_service import get_answer; print(get_answer('ABCDEFGHIJKLMNOPQRSTU'))"

Expected and observed output:

    Please enter an ACH return code of 20 characters or fewer.

## Normal Configuration After Testing

- MODEL_NAME = "gemma3:4b"
- timeout = 120.0
- answer = (response.message.content or "").strip()

Temporary test changes were restored, and normal responses
were confirmed after each error test.

## Testing Limitations

- These results cover manual tests and one direct function check.
- An automated pytest suite has not yet been run.
- Unexpected exceptions and non-404 Ollama errors were not simulated.
- No real customer data or banking systems were used.
- Source links were displayed; website availability was not tested.
- The app does not verify the state of a real transaction.
- RAG testing is outside the current MVP scope.