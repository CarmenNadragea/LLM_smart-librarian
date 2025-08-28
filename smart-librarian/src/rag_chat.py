"""
rag_chat.py
Orchestrare RAG + GPT + tool-calling pentru recomandări de cărți.
"""
import os
from openai import OpenAI
from dotenv import load_dotenv
from src.loader import get_retriever
from src.tools import get_summary_by_title

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=OPENAI_API_KEY)


def retrieve_books(query, k=3):
    """
    Folosește ChromaDB pentru a găsi cele mai relevante rezumate de cărți.
    :param query: Interesul/temele utilizatorului
    :param k: Număr de rezultate
    :return: Listă dicturi cu titlu și rezumat
    """
    retriever = get_retriever()
    # Creează embedding OpenAI pentru query
    from src.loader import get_embeddings
    query_embedding = get_embeddings([query])[0]
    results = retriever.query(
        query_embeddings=[query_embedding],
        n_results=k
    )
    books = []
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        books.append({"title": meta["title"], "summary": doc})
    return books


def gpt_recommend(query, candidates):
    """
    Trimite contextul + query la GPT. GPT alege o singură carte și o recomandă.
    :param query: Întrebarea utilizatorului
    :param candidates: Listă dicturi cu titlu și rezumat
    :return: dict cu titlu recomandat și motivare
    """
    system_prompt = (
        "Ești un asistent AI care recomandă o singură carte din lista de candidați, pe baza interesului utilizatorului. "
        "Răspunde scurt, menționând titlul exact și motivul alegerii. Nu inventa titluri."
    )
    context = "\n".join([f"Titlu: {b['title']}\nRezumat: {b['summary']}" for b in candidates])
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Interes: {query}\nCărți candidate:\n{context}"}
    ]
    response = openai_client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=messages,
        tools=[{
            "type": "function",
            "function": {
                "name": "get_summary_by_title",
                "description": "Returnează rezumatul complet pentru titlul exact.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"}
                    },
                    "required": ["title"]
                }
            }
        }],
        tool_choice="auto"
    )
    # Extrage titlul recomandat din răspuns
    import json
    choice = response.choices[0]
    tool_calls = getattr(choice.message, "tool_calls", None)
    title = None
    reason = choice.message.content
    if tool_calls:
        # GPT a apelat tool-ul
        args = tool_calls[0].function.arguments
        if isinstance(args, str):
            try:
                args = json.loads(args)
            except Exception:
                args = {}
        title = args.get("title")
    if not title:
        # Fallback: extrage titlul din răspuns
        import re
        match = re.search(r"(?:Titlu:|title:|recomand|recomandă)\s*([\w\s\d]+)", reason, re.IGNORECASE)
        for b in candidates:
            if b["title"].lower() in reason.lower():
                title = b["title"]
                break
        if not title and match:
            title = match.group(1).strip()
    return {"title": title, "reason": reason}


def get_full_recommendation(query):
    """
    Orchestrare completă: retrieval, GPT, tool, răspuns final.
    :param query: Întrebarea utilizatorului
    :return: dict cu recomandare scurtă și rezumat complet
    """
    candidates = retrieve_books(query)
    rec = gpt_recommend(query, candidates)
    summary = get_summary_by_title(rec["title"])
    short = rec["reason"]
    if not short or short.strip().lower() == "none":
        if rec["title"]:
            short = f"Recomand cartea: {rec['title']}"
        else:
            short = "Vezi rezumatul de mai jos."
    return {
        "short": short,
        "summary": summary or "Rezumat indisponibil."
    }
