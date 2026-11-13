# SchemeSathi AI 🇮🇳
### AI-Powered Government Scheme Discovery and Assistance Platform

**SchemeSathi AI** is an AI-powered assistant designed to simplify access to government welfare schemes. It helps users discover relevant Central and State Government schemes, understand eligibility requirements, explore application procedures and find useful supporting information through a conversational interface.

The platform combines AI-assisted query understanding, a curated scheme knowledge base and retrieval-based information access to make government benefits easier to navigate.

---

## 1. Problem Statement

Government welfare schemes are distributed across multiple portals and departments. Citizens often face difficulties identifying schemes relevant to their circumstances, understanding eligibility criteria, locating application procedures and identifying the documents required.

This creates an information gap between available public benefits and the people who may qualify for them.

## 2. Proposed Solution

SchemeSathi AI provides a centralized, conversational platform that helps users explore government schemes using natural-language queries.

The system retrieves relevant scheme information from its knowledge base and uses AI-assisted processing to make the information easier to understand.

It aims to improve awareness, accessibility and navigation of government welfare information.

## 3. Project Objectives

- Simplify the discovery of government welfare schemes.
- Provide understandable eligibility information.
- Assist users in navigating application procedures.
- Organize scheme information in a searchable knowledge base.
- Support document-based information extraction.
- Provide conversational assistance through an AI interface.
- Encourage users to verify important information through official government sources.

## 4. Key Features

### 4.1 Discover Schemes
Browse and search a curated directory of government schemes using user queries, state selection and category filters.

### 4.2 Eligibility Checker
Assist users in understanding scheme eligibility requirements based on the information they provide.

### 4.3 Application Guide
Present application-related guidance, including steps and supporting information where available.

### 4.4 Ask SchemeSathi
An AI-powered conversational interface that allows users to ask questions about government schemes in natural language.

### 4.5 Saved Schemes
Provides a workspace for keeping track of schemes of interest.

### 4.6 Document Upload
Supports uploading documents for information extraction and knowledge-based assistance.

### 4.7 Retrieval-Augmented Generation (RAG)
Uses a retrieval-based approach to identify relevant information from the scheme knowledge base before generating AI-assisted responses.

## 5. Technology Stack

| Component | Technology |
|---|---|
| Frontend and UI | Streamlit |
| Programming Language | Python |
| AI Model Integration | Google Gemini API |
| Vector Database | ChromaDB |
| Embedding Model | Sentence Transformers |
| Document Processing | PyPDF |
| Environment Configuration | Python Dotenv |
| Testing | Pytest |
| Version Control | Git and GitHub |

## 6. System Architecture

The application follows a modular architecture.

**User Interface Layer**
- Streamlit application
- User query input
- Scheme discovery and navigation
- Document upload interface

**Application and Agent Layer**
- Query understanding
- Eligibility assistance
- Application guidance
- Service orchestration

**Knowledge and Retrieval Layer**
- Curated government scheme records
- Text embeddings
- ChromaDB vector storage
- Retrieval of relevant information

**AI Response Layer**
- Gemini API integration
- Context-aware response generation
- Retrieval-based fallback when AI services are unavailable

### Workflow

1. The user enters a query or selects a feature.
2. The application processes the request.
3. Relevant scheme information is retrieved from the knowledge base.
4. AI-assisted processing generates an understandable response when the Gemini service is available.
5. The user receives scheme-related information and guidance.

## 7. Project Structure

```text
SchemeSathi-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
├── run_windows.bat
│
├── core/
│   ├── __init__.py
│   ├── agents.py
│   ├── knowledge.py
│   ├── service.py
│   └── ui.py
│
├── data/
│   └── schemes.json
│
├── tests/
│   └── test_project.py
│
└── .streamlit/
    └── config.toml
```

## 8. Installation and Setup

### Prerequisites

- Python 3.10 or later, subject to dependency compatibility
- Git
- Google Gemini API key
- Internet connection for downloading required models and accessing the AI service

### Step 1: Clone the repository

```bash
git clone https://github.com/carol-bug/SchemeSathi-AI.git
cd SchemeSathi-AI
```

### Step 2: Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure environment variables

Create a `.env` file using `.env.example` as the template.

Add your Gemini configuration:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=your_supported_gemini_model
```

Use a model ID currently supported by your Google AI Studio account.

**Security note:** Never upload your `.env` file or expose your API key in a public repository.

### Step 5: Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal to access SchemeSathi AI.

## 9. Testing

Run the project's test suite using:

```bash
pytest -q
```

To check Python syntax:

```bash
python -m compileall app.py core
```

## 10. Current Scope and Limitations

- The current knowledge base contains six curated scheme records.
- Scheme coverage is currently limited and does not represent a complete government scheme directory.
- Eligibility results are preliminary guidance and do not constitute official eligibility approval.
- Scheme benefits, deadlines and application requirements may change.
- AI-generated responses depend on available model access and retrieved information.
- Users should verify all important details through the relevant official government portals.
- The application is currently an academic prototype.

## 11. Future Enhancements

- Expand the knowledge base with verified Central and State Government schemes.
- Integrate official government APIs and regularly updated scheme information where available.
- Improve eligibility matching using structured user profiles.
- Add multilingual support for Indian languages.
- Enhance document extraction and document-based eligibility assistance.
- Introduce secure user authentication and personalized saved schemes.
- Add deployment and monitoring capabilities.
- Improve source citations and traceability for generated responses.

## 12. Disclaimer

SchemeSathi AI is an academic prototype developed for educational and demonstration purposes. It is not affiliated with or endorsed by any government department.

The information provided by the application is indicative and should not be treated as official advice, an eligibility guarantee or confirmation of benefit approval.

Always consult official government portals and authorities before applying.

---

## 13. Repository

**GitHub:** https://github.com/carol-bug/SchemeSathi-AI

**Project:** SchemeSathi AI — Public Benefits, Made Simple.

