"""
loader.py
Încarcă rezumatele din book_summaries.md și populează ChromaDB cu embeddings OpenAI.
"""
import os
import chromadb
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = chromadb.PersistentClient(path=os.path.join(os.path.dirname(__file__), "..", "chromadb_store"))
openai_client = OpenAI(api_key=OPENAI_API_KEY)

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "book_summaries.md")


def parse_book_summaries(md_path):
    """Parsează fișierul Markdown și returnează lista de dicturi cu titlu și rezumat."""
    books = []
    with open(md_path, encoding="utf-8") as f:
        lines = f.readlines()
    title, summary = None, []
    for line in lines:
        if line.startswith("## Title:"):
            if title and summary:
                books.append({"title": title, "summary": " ".join(summary).strip()})
            title = line.replace("## Title:", "").strip()
            summary = []
        elif line.strip():
            summary.append(line.strip())
    if title and summary:
        books.append({"title": title, "summary": " ".join(summary).strip()})
    return books


def get_embeddings(texts):
    """Creează embeddings folosind OpenAI text-embedding-3-small."""
    response = openai_client.embeddings.create(
        input=texts,
        model="text-embedding-3-small"
    )
    return [e.embedding for e in response.data]


def load_chromadb():
    """Încarcă rezumatele în ChromaDB cu embeddings."""
    books = parse_book_summaries(DATA_PATH)
    summaries = [b["summary"] for b in books]
    titles = [b["title"] for b in books]
    embeddings = get_embeddings(summaries)
    collection = client.get_or_create_collection(name="books", embedding_function=None)
    for i, (title, summary, emb) in enumerate(zip(titles, summaries, embeddings)):
        collection.add(
            ids=[str(i)],
            embeddings=[emb],
            documents=[summary],
            metadatas=[{"title": title}]
        )
    if hasattr(collection, 'persist'):
        collection.persist()
    return collection


def get_retriever():
    """Returnează retriever semantic pentru căutare."""
    collection = client.get_collection("books")
    return collection
