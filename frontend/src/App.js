import './App.css';
import { useState } from 'react';

function App() {
  const [link, setLink] = useState("");

  const enviar = async (e) => {
    e.preventDefault();
    const dado = { link };

    try {
      const resposta = await fetch("http://localhost:5000/download", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(dado)
      });
      if (!resposta.ok) {
        throw new Error("Erro ao baixar vídeo");
      }
      // Aqui você pode tratar a resposta, por exemplo, baixar o arquivo
      alert("Download iniciado!");
    } catch (erro) {
      alert("Erro: " + erro.message);
    }
  };

  return (
    <div className="App">
      <header>
        <a href="">
          <h1>Downloader Youtube</h1>
        </a>
      </header>
      <main>
        <div className="container">
          <div className="form">
            <h2>Download Youtube Videos</h2>
            <form onSubmit={enviar}>
              <input
                type="text"
                name="url"
                placeholder="Insira o link do vídeo"
                onChange={(e) => setLink(e.target.value)}
                required
              />
              <button type="submit">Download</button>
            </form>
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
