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
      setResponse(data.recommendation || JSON.stringify(data));
    } catch (err) {
      setResponse('Eroare la comunicarea cu backend-ul.');
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <div className="card">
        <h1 className="title">Smart Librarian</h1>
        <form onSubmit={handleSubmit} className="form">
          <input
            type="text"
            className="input"
            placeholder="Scrie o întrebare despre cărți..."
            value={query}
            onChange={e => setQuery(e.target.value)}
            required
          />
          <button className="button" type="submit" disabled={loading}>
            {loading ? 'Se caută...' : 'Cere recomandare'}
          </button>
        </form>
        {response && (
          <div className="response">
            <h2>Recomandare:</h2>
            <p>{response}</p>
          </div>
        )}
      </div>
      <footer className="footer">&copy; 2025 Smart Librarian</footer>
    </div>
  );
}

export default App;
