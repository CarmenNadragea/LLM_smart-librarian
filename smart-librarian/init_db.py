"""
init_db.py
Populează ChromaDB cu rezumatele din book_summaries.md.
"""

import os
from src.loader import load_chromadb

if __name__ == "__main__":
    try:
        collection = load_chromadb()
        chroma_path = os.path.join(os.path.dirname(__file__), "chromadb_store")
        if os.path.exists(chroma_path):
            print(f"ChromaDB populat cu rezumate! Folderul există: {chroma_path}")
        else:
            print(f"ATENȚIE: ChromaDB nu a creat folderul: {chroma_path}")
        print(f"Colecții disponibile: {getattr(collection, 'name', None)}")
    except Exception as e:
        print(f"Eroare la popularea ChromaDB: {e}")
