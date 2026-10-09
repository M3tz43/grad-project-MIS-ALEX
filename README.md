# Résumé–Job Skill Matching Prototype

Graduation-project prototype exploring how natural-language processing can extract skills from résumés and compare them with the requirements of a job description.

## Project status

This repository contains an early proof of concept. The existing scripts demonstrate the intended processing steps, but the project is **not yet runnable end to end** because configuration, sample data and several shared variables are missing. A structured rebuild is planned before this project is presented as a finished portfolio application.

## Intended workflow

1. Extract text from PDF or Word résumés.
2. Process the text with spaCy.
3. Identify skills with custom `EntityRuler` patterns.
4. Extract required skills from a job description.
5. Compare candidate and job skill sets.
6. Calculate and display a skill-match percentage.

## Current files

- `read.py` — PDF and Word text extraction functions
- `tokenize.py` — spaCy model loading and résumé tokenization
- `match.py` — custom skill-entity matching
- `recommend.py` — match scoring logic
- `main.py` — experimental combined workflow

## Planned rebuild

- Consolidate the scripts into a clear Python package.
- Replace deprecated PDF APIs.
- Add configuration and command-line arguments.
- Include anonymized example résumés and job descriptions.
- Add `requirements.txt`, automated tests and type hints.
- Add evaluation metrics for skill-extraction quality.
- Document privacy, fairness and model limitations.

## Responsible-use note

This project is intended as a decision-support experiment, not an automated hiring system. A match percentage cannot measure a person's overall suitability, and any future implementation should be evaluated for bias, privacy and accessibility risks.

