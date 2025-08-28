"""
main.py - FastAPI backend pentru Smart Librarian
Expune endpoint /recommend pentru recomandare carte + rezumat.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.rag_chat import get_full_recommendation

app = FastAPI()

# Permite request-uri din frontend (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class RecommendRequest(BaseModel):
    query: str

@app.post("/recommend")
async def recommend(req: RecommendRequest):
    try:
        result = get_full_recommendation(req.query)
        return result
    except Exception as e:
        import traceback
        print("[ERROR] /recommend:", e)
        traceback.print_exc()
        return {"error": str(e), "trace": traceback.format_exc()}

@app.post("/test")
async def test_endpoint(data: dict):
    return {"status": "ok", "data": data}
