# Rebuild roadmap

## Phase 1 — Make the prototype runnable

- Define the project directory through configuration instead of global variables.
- Add the missing skill-pattern file and anonymized sample inputs.
- Replace `PyPDF2.PdfFileReader` with the current `pypdf` API.
- Remove duplicated code and unresolved variables.
- Add a minimal command-line interface.

## Phase 2 — Improve engineering quality

- Add dependency management and supported Python versions.
- Add unit tests for extraction, normalization and match scoring.
- Add logging and actionable error messages.
- Separate data loading, NLP processing and reporting.

## Phase 3 — Evaluate the method

- Create a labeled evaluation set.
- Report precision, recall and F1 for skill extraction.
- Compare exact matching with normalized and semantic matching.
- Document limitations and potential sources of bias.

