import React, { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponse('');
    try {
      const res = await fetch('http://127.0.0.1:8000/recommend', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
      });
      const data = await res.json();
      if (data.short || data.summary) {
        setResponse(
          (data.short ? `Recomandare: ${data.short}\n` : '') +
          (data.summary ? `Rezumat: ${data.summary}` : '')
        );
      } else {
        setResponse(JSON.stringify(data));
      }
    } catch (err) {
      setResponse('Eroare la comunicarea cu backend-ul.');
    }
    setLoading(false);
  };

  return (
    <div className="main-bg">
      <div className="center-container">
        <div className="card-modern">
          <div className="title-modern">
            <span>Smart</span>
            <span className="title-accent">Librarian</span>
          </div>
          <div className="subtitle">
            Recomandări de cărți cu AI. Scrie o întrebare și primește sugestii
            personalizate!
          </div>
          <form onSubmit={handleSubmit} className="form-modern-col">
            <input
              type="text"
              className="input-modern"
              placeholder="Ex: vreau o carte SF"
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              required
            />
            <button className="button-modern" type="submit" disabled={loading}>
              {loading ? (
                <span className="loader" />
              ) : (
                'Cere recomandare'
              )}
            </button>
          </form>
          {response && (
            <div className="response-modern">
              <h2>Recomandare:</h2>
              <p>{response}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
