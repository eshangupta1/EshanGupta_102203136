# AI Furniture Recommendation System

This is a complete **end-to-end AI/ML web application** that recommends furniture products based on user queries, generates AI-powered product descriptions, and visualizes dataset insights through an interactive UI.

The project combines:
✅ Machine Learning (model training)
✅ NLP Embeddings
✅ Vector Search
✅ Generative AI
✅ FastAPI Backend
✅ React Frontend
✅ Data Analytics Dashboard

---

## 🚀 Main Features

### 🔹 1. Product Recommendation (Semantic Search)
- Converts product text into embeddings
- Converts user query into embedding
- Finds similar products using vector similarity (FAISS / vector DB)
- Supports filtering (e.g. “modern wooden table under 20000”)

### 🔹 2. AI-Powered Product Descriptions
- Generates marketing-style blurbs for each recommended product
- Uses a local or external language model
- Makes results readable and engaging

### 🔹 3. Interactive Frontend (React)
- `/chat` → Chat-style product recommendation interface
- `/viz` → Analytics dashboard with charts (prices, brands, categories, etc.)
- Built with React + Vite + Tailwind + Recharts

### 🔹 4. FastAPI Backend
- `/ingest` → Load CSV, clean data, embed products, store vectors
- `/recommend` → Return top product matches
- `/generate` → AI-based product description
- `/analytics/summary` → Stats for dashboard
- `/docs` → Auto API documentation (Swagger UI)

### 🔹 5. Model Training Notebook (Required in PDF)
- `train_models.ipynb`
- Trains a text classification model (TF-IDF + Logistic Regression)
- Predicts categories from product descriptions
- Shows accuracy + confusion matrix
- Saves trained model artifact

### 🔹 6. Analytics Notebook
- `analytics.ipynb`
- Exploratory data analysis
- Price distribution, top categories, brands
- Embedding visualization or clustering (optional)

---

## 📂 Project Structure (Important)

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


Then open browser at the shown URL:
- `/chat` → recommendations
- `/viz` → analytics dashboard

---

## 🧠 Technologies Used

**Backend:** FastAPI, Python, SentenceTransformers, FAISS  
**Frontend:** React, Vite, Tailwind CSS, Recharts  
**ML:** Scikit-learn, Logistic Regression, embeddings  
**Generative AI:** Local or external language model  
**Notebooks:** Jupyter (EDA + training)

---

## ✅ Why This Project Stands Out

✔ Full-stack AI application (not just a model)  
✔ Real product recommendation logic  
✔ NLP + ML + Generative AI integration  
✔ Production-style architecture  
✔ Easy to run and extend  
✔ Clean modular code  
✔ Meets all PDF requirements

---

## ✅ Future Enhancements (optional ideas)
- CLIP-based image similarity
- Personalized recommendations
- Cross-encoder reranking
- User feedback loop
- Cloud deployment

---

## 🎯 Summary

This project demonstrates the complete lifecycle of an AI-powered product recommendation system:
**Data → Embeddings → ML training → Vector search → Generative AI → Web App → Analytics**

It showcases strong skills in:
✅ Machine Learning  
✅ NLP / AI  
✅ Backend engineering  
✅ Frontend development  
✅ System design  

**Perfect for real-world applications and interview evaluation.**

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
