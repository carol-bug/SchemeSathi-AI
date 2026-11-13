# SchemeSathi AI — Public benefits, made simple

A polished Streamlit prototype for discovering Indian public-benefit schemes, reviewing preliminary eligibility signals, understanding application steps, asking grounded questions and indexing official PDF documents.

## Product modules
- Discover schemes with natural-language search, state/category filters, scheme cards and a saved shortlist.
- Eligibility checker for preliminary screening against available structured rules.
- Application guide with stepwise checklist and official source links.
- Conversational Ask SchemeSathi experience, grounded in retrieved scheme records.
- Saved schemes shortlist for the current browser session.
- PDF upload and text extraction into persistent ChromaDB.
- About page with architecture, technology and responsible-use notes.

## Architecture
Streamlit UI → Query Understanding Agent → Retrieval Agent (ChromaDB + local Sentence Transformers; keyword fallback) → Eligibility/Application Agents → optional Gemini response generation.

The Gemini client is cached on the service instance and reused. If the key is absent or Gemini fails, the app falls back to local source-linked retrieval instead of crashing.

## Setup — Windows PowerShell
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```
Edit `.env` and add your Gemini API key from Google AI Studio. Keep `.env private and out of Git.

Run:
```powershell
streamlit run app.py
```

## Gemini model
The default in `.env.example` is `gemini-3.8-flash` because the development API error explicitly recommended this model. Model availability is account/project-specific. If it is unavailable, change `GEMINI_MODEL` to an exact model ID enabled in your Google AI Studio project. The app remains usable in retrieval-only mode if Gemini is unavailable.

## Knowledge base
Curated starter records are in `data/schemes.json`. The app attempts to initialise ChromaDB with local `all-MiniLM-L6-v2` embeddings. First use may download model weights. If vector setup fails, keyword retrieval remains active. Uploaded PDF text is indexed in the persistent collection.

## Checks
```powershell
python -m compileall app.py core
pytest -q
```

## Limitations and responsible use
- Academic prototype, not an official government service.
- Starter dataset is curated and not a complete live database.
- Eligibility checks are preliminary and incomplete; only the relevant authority decides eligibility.
- No live beneficiary database access, application submission or status tracking.
- Scanned PDF OCR is not included.
- Verify benefit amounts, eligibility, deadlines and document lists on official portals.
- Do not upload Aadhaar numbers, bank details, OTPs or other sensitive personal information.
