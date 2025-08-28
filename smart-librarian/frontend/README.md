# Frontend Smart Librarian

Acest folder este destinat aplicației frontend (React, Vue, Angular etc.) care va consuma API-ul FastAPI expus de backend.

## Exemplu structură React
- `src/` - cod sursă React
- `public/` - fișiere statice
- `package.json` - dependențe

## Pornire rapidă
1. Din acest folder, rulează:
   ```
   npx create-react-app .
   ```
2. Adaugă cod pentru request către backend (ex: folosind `fetch` sau `axios`).
3. Rulează cu:
   ```
   npm start
   ```

Backend-ul trebuie să fie pornit pe `http://localhost:8000`.
