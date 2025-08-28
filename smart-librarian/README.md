# Smart Librarian – AI cu RAG + Tool

Un chatbot AI care recomandă cărți pe baza intereselor utilizatorului, folosind OpenAI GPT, RAG cu ChromaDB și un tool pentru rezumate detaliate.

## Arhitectură
```
smart-librarian/
├── backend/
│   ├── main.py         # FastAPI backend, endpoint /recommend
│   ├── requirements.txt
│   └── ...
├── frontend/
│   ├── src/App.js      # React UI modern, interactiv
│   ├── src/App.css     # Design modern, gradient, fonturi Google
│   └── ...
├── app.py              # CLI
├── streamlit_app.py    # UI Streamlit
├── .env                # Cheie OpenAI
├── README.md
├── data/
│   └── book_summaries.md
└── src/
    ├── loader.py
    ├── tools.py
    └── rag_chat.py
```

## Instalare și configurare

1. Instalează dependențele backend:
   ```
   pip install -r backend/requirements.txt
   ```
2. Instalează dependențele frontend:
   ```
   cd frontend
   npm install
   ```
3. Creează fișier `.env` în rădăcina proiectului cu:
   ```
   OPENAI_API_KEY=your_openai_key
   ```
   (cheia se obține de la https://platform.openai.com/account/api-keys)

## Rulare completă

### Backend FastAPI
```powershell
cd backend
uvicorn main:app --reload
```
Backend-ul rulează pe http://127.0.0.1:8000

### Frontend React
```powershell
cd frontend
npm start
```
Frontend-ul rulează pe http://localhost:3000

### Test conexiune backend
- Poți testa endpoint-ul `/test` cu Postman sau direct din frontend (buton de test).
- Pentru recomandări AI, asigură-te că ai o cheie OpenAI validă în `.env`.

### CLI
```bash
python app.py
```

### UI Streamlit
```bash
streamlit run streamlit_app.py
```

## Endpointuri principale
- `POST /recommend` – primește `{ "query": "..." }` și returnează recomandare + rezumat
- `POST /test` – test conexiune backend

## Exemple întrebări
- Vreau o carte despre libertate și control social.
- Ce-mi recomanzi dacă iubesc poveștile fantastice?
- Ce este 1984?
- Ce recomanzi pentru cineva care iubește povești de război?

## Tehnologii
- FastAPI
- React
- openai
- chromadb
- tiktoken
- streamlit
- python-dotenv

## Output chatbot
1. Recomandare scurtă (GPT)
2. Rezumat complet (tool)

## UI Modern
- Gradient roz, fonturi Quicksand/Roboto/Poppins
- Card interactiv, animații titlu, layout responsive

## Troubleshooting
- Dacă primești eroare 401 la /recommend, verifică cheia OpenAI din `.env`.
- Poți testa conexiunea cu `/test` chiar fără cheie OpenAI.
