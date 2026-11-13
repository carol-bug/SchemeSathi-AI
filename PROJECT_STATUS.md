# Build and verification status

## Verified in the current build environment
- All Python files compile successfully with Python 3.13.5 (`python -m compileall -q .`).
- Seven automated unit tests pass (`pytest -q`).
- Tests cover intent routing, conservative eligibility checks and source metadata presence.

## Not verified in this environment
The environment has no network access and the following dependencies are not installed: Streamlit, LangChain, LangChain Google GenAI, LangChain Chroma, LangChain Hugging Face, ChromaDB and Sentence Transformers. A package installation attempt failed because package-index DNS/network access is unavailable.

Therefore the following still require verification on a laptop with internet access:
- Dependency installation and version compatibility.
- Download of `all-MiniLM-L6-v2` on first run.
- ChromaDB vector persistence and similarity retrieval.
- Gemini API authentication, model availability and quota.
- Live Streamlit startup and end-to-end agent execution.
- Uploaded PDF indexing and source-grounded LLM answers.

Do not represent these integration checks as passed until run locally.
