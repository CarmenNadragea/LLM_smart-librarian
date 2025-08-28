# Smart Librarian – AI cu RAG + Tool

Un chatbot AI care recomandă cărți pe baza intereselor utilizatorului, folosind OpenAI GPT, RAG cu ChromaDB și un tool pentru rezumate detaliate.

## Instalare

1. Instalează dependențele:
   ```
   pip install -r requirements.txt
   ```
2. Exportă cheia OpenAI:
   ```
   set OPENAI_API_KEY=your_openai_key
   ```
   (sau folosește un fișier `.env` cu `OPENAI_API_KEY=...`)

## Rulare CLI
```bash
python app.py
```

## Rulare UI Streamlit
```bash
streamlit run streamlit_app.py
```

## Exemple întrebări
- Vreau o carte despre libertate și control social.
- Ce-mi recomanzi dacă iubesc poveștile fantastice?
- Ce este 1984?
- Ce recomanzi pentru cineva care iubește povești de război?

## Arhitectură
```
smart-librarian/
├── app.py
├── streamlit_app.py
├── requirements.txt
├── README.md
├── data/
│   └── book_summaries.md
└── src/
    ├── loader.py
    ├── tools.py
    └── rag_chat.py
```

## Tehnologii
- openai
- chromadb
- tiktoken
- streamlit
- python-dotenv

## Output chatbot
1. Recomandare scurtă (GPT)
2. Rezumat complet (tool)
