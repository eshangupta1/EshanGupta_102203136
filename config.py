import os
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    USE_PINECONE: bool = os.getenv("USE_PINECONE","false").lower()=="true"
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY","")
    PINECONE_ENV: str = os.getenv("PINECONE_ENV","us-east-1-gcp")
    PINECONE_INDEX_TEXT: str = os.getenv("PINECONE_INDEX_TEXT","furniture-reco")

    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER","hf")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY","")
    HF_GENERATION_MODEL: str = os.getenv("HF_GENERATION_MODEL","google/flan-t5-base")

    DATA_CSV: str = os.getenv("DATA_CSV","../data/raw.csv")
    CORS_ORIGINS: List[str] = os.getenv("CORS_ORIGINS","*").split(",")

settings = Settings()
