# APISIX Schema Form Engine

APISIX Schema Form Engine is a backend service that converts APISIX-style JSON schemas
into structured form definitions consumable by frontend applications.

The goal of this project is to reduce manual UI development by programmatically
deriving form layouts, field metadata, and conditional logic directly from schema
definitions used in API gateways.

This project is inspired by schema-driven configuration workflows used in
Apache APISIX, but is currently an independent implementation.

---

## Features

- Parse primitive schema fields (string, number, boolean)
- Support `oneOf` conditional schema structures
- Resolve field dependencies
- Generate deterministic, frontend-ready form definitions
- Fully tested backend logic using pytest

---

## Project Structure
apisix-schema-form-engine/
└── backend/
    ├── app/
    │   ├── main.py                 # FastAPI application entry point
    │   ├── api/
    │   │   └── generate_form.py    # API endpoint to generate form definitions
    │   └── parser/
    │       ├── primitives.py       # Primitive schema field parsing
    │       ├── oneof.py            # oneOf schema handling logic
    │       └── dependencies.py     # Dependency resolution logic
    ├── tests/
    │   ├── test_primitives.py      # Tests for primitive parsing
    │   ├── test_oneof.py           # Tests for oneOf logic
    │   └── test_dependencies.py   # Tests for dependency handling
    ├── LICENSE                     # Apache License 2.0
    ├── NOTICE                      # ASF notice file
    ├── DISCLAIMER                  # ASF disclaimer
    ├── README.md                   # Project documentation
    └── requirements.txt            # Python dependencies
---

## Tech Stack

- Python 3.10+
- FastAPI
- Pytest

---

## Status

This project is under active development.
Frontend integration and extended schema support are planned.

---

## Disclaimer

This project is not affiliated with, endorsed by, or sponsored by the
Apache Software Foundation.

Apache®, APISIX®, and related trademarks are the property of
The Apache Software Foundation.

this is a test change to create a PR