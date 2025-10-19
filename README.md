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


🚀 Main Features
✅ 1. Content-Based Product Recommendations

Converts product text (title + description) into vector embeddings.

Converts user query into same embedding space.

Finds most similar products (FAISS / vector search).

Supports filtering by price or category.

✅ 2. AI-Generated Product Descriptions

Automatically writes a natural language blurb for each product.

Uses a local language model or external API.

Makes results more human-friendly and marketing-style.

✅ 3. Analytics Dashboard

Visualizes dataset insights:

Top brands

Top categories

Price distribution

Materials/colors

Built with Recharts in the frontend and summary API in backend.

✅ 4. Model Training Notebook (Required in PDF)

train_models.ipynb trains a text classification model:

TF-IDF + Logistic Regression

Predicts categories from text

Shows accuracy, confusion matrix

Saves model artifact

Demonstrates real ML training process.

✅ 5. Modern Web UI

React frontend with two main pages:

/chat → Chat-style recommendation interface

/viz → Analytics dashboard with charts

Responsive design with Tailwind CSS.

✅ 6. FastAPI Backend

REST API endpoints:

/ingest → load CSV, embed items, store vectors

/recommend → return top product matches

/generate → AI-generated description

/analytics/summary → stats for charts

✅ 7. Clean Architecture & Modular Code

Separate layers:

routers/ → API endpoints

models/ → embedding models / ML utilities

services/ → vector search, schemas, business logic

Easy to maintain and extend.

project/
│
├─ backend/
│  ├─ app.py                  # Main FastAPI application
│  ├─ config.py               # Environment settings
│  ├─ routers/
│  │   ├─ ingest.py           # CSV → embedding → vector store
│  │   ├─ recommend.py        # Recommendation endpoint
│  │   ├─ generate.py         # AI description generation
│  │   └─ analytics.py        # Stats for dashboard
│  ├─ models/
│  │   ├─ embed_text.py       # Text embedding model
│  │   └─ (optional) embed_image.py (CLIP)
│  ├─ services/
│  │   ├─ vector_store.py     # FAISS / vector DB wrapper
│  │   ├─ schemas.py          # Pydantic request/response models
│  │   └─ retrieval.py        # (optional) ranking logic
│  ├─ requirements.txt        # Backend dependencies
│  └─ .env.example            # Config template
│
├─ frontend/
│  ├─ src/
│  │   ├─ routes/
│  │   │   ├─ Chat.tsx        # Chat UI for recommendations
│  │   │   └─ Analytics.tsx   # Charts dashboard
│  │   ├─ components/
│  │   │   ├─ ProductCard.tsx # Display product with AI copy
│  │   │   └─ ChatInput.tsx   # Input component
│  │   ├─ api.ts              # Axios API calls to backend
│  │   └─ App.tsx / main.tsx  # Routing setup
│  ├─ package.json            # Frontend dependencies
│  └─ .env.example            # API base URL template
│
├─ notebooks/
│  ├─ analytics.ipynb         # EDA, visualizations, insights
│  └─ train_models.ipynb      # Model training (required)
│
├─ data/
│  └─ raw.csv (local only, not committed)
│
├─ README.md                  # Project documentation (this file)
└─ .gitignore                 # Ignore env, node_modules, etc.


✅ End-to-End Flow

1️⃣ Load raw product data (CSV)
2️⃣ Clean and embed product text
3️⃣ Store embeddings in vector search index
4️⃣ User types natural language query
5️⃣ Backend finds similar items via vector similarity
6️⃣ AI generates description for each item
7️⃣ Frontend shows results in chat format
8️⃣ Analytics page visualizes overall dataset insights
9️⃣ Notebook demonstrates ML model training

=> Complete ML + AI + Web application.
