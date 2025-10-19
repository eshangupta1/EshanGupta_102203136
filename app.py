from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
from routers import ingest, recommend, generate, analytics

app = FastAPI(title="AI Furniture Reco (Fast)")
app.add_middleware(CORSMiddleware, allow_origins=settings.CORS_ORIGINS,
                   allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(ingest.router, prefix="/api")
app.include_router(recommend.router, prefix="/api")
app.include_router(generate.router, prefix="/api")
app.include_router(analytics.router, prefix="/api")
