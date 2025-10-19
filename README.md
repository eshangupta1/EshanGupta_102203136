# FurnishAI — Fast, Self-Contained Build (Windows-ready)

- FAISS default (no keys). Pinecone optional.
- Local GenAI (flan-t5-base). OpenAI optional.
- FastAPI backend + React/Tailwind frontend.
- Chat UI + Analytics page.

## Run (Windows PowerShell)
1) Backend
```
cd backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
copy .env.example .env
uvicorn app:app --reload --port 8000
```
2) Ingest
```
Invoke-WebRequest -Method POST http://localhost:8000/api/ingest
```
3) Frontend
```
cd ..rontend
npm install
copy .env.example .env
npm run dev
```
Open http://localhost:5173 → Chat / Analytics.
