# SchemeSathi AI — Viva Preparation

## Problem statement
Public scheme information is distributed across government portals and notifications. SchemeSathi provides a single discovery and guidance interface over a curated local knowledge base.

## Modules
1. Discover schemes using natural-language search and state/category filters.
2. Eligibility checker for preliminary rule-based screening.
3. Application guide with practical next steps and official source links.
4. Ask SchemeSathi conversational Q&A.
5. Saved schemes shortlist.
6. PDF ingestion for text-based official scheme documents.
7. About page explaining architecture and limitations.

## Agentic workflow
- Query Understanding Agent extracts state, profile and intent signals.
- Retrieval Agent searches local ChromaDB vectors with local Sentence Transformers and keyword fallback.
- Eligibility Agent compares user answers with structured rule fields.
- Application Agent creates a stepwise process based on the indexed scheme record.
- Optional Gemini generation receives retrieved records as context and is instructed not to invent missing details.

## RAG
Retrieval-Augmented Generation retrieves scheme records before calling the language model. This grounds generated answers in the local knowledge base. RAG reduces unsupported responses but does not guarantee completeness or freshness.

## Why local embeddings and ChromaDB?
Sentence Transformers generate embeddings locally; ChromaDB persists vectors and metadata on disk. This avoids paid embedding API calls and allows reuse between sessions. First-time model weights may need to be downloaded.

## Gemini failure handling
The Gemini client is created once and cached on the service instance. If no key is configured or a model/network error occurs, the app uses a local retrieval-based response and displays a notice.

## Limitations
- Curated starter records are not a complete live government database.
- Eligibility screening is not an official decision.
- No beneficiary database access, live application submission or status tracking.
- Scanned PDF OCR is not implemented.
- Scheme details can change; verify with official sources.

## Demo queries
- I am a farmer in Karnataka. What support schemes can help me?
- Explain PM-KISAN and where I can verify beneficiary status.
- I am an unemployed graduate in Karnataka. Which programme should I check?
- How do I verify whether my family is eligible for PM-JAY?

## Key viva statement
"SchemeSathi AI is a source-grounded discovery and guidance prototype. It helps users navigate information but does not make official eligibility decisions. Final rules and decisions remain with the relevant government department."
