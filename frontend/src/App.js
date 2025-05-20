import './App.css';
import { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faMagnifyingGlass } from '@fortawesome/free-solid-svg-icons';


function App() {
  const [link, setLink] = useState("");
  const [thumb, setThumb] = useState("");
  const [titulo, setTitulo] = useState("");
  const [dir, setDir] = useState("");
  const [carregando, setCarregando] = useState(false);

  const enviar = async (e) => {
    e.preventDefault();
    setCarregando(true);
    setDir(""); // Limpa link anterior

    try {
      const resposta = await fetch("http://localhost:5000/download", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ link })
      });

      if (!resposta.ok) {
        throw new Error("Erro ao baixar vídeo");
      }

      const dados = await resposta.json();
      setThumb(dados.thumb);
      setTitulo(dados.titulo);
      setDir("http://localhost:5000/pasta_videos/" + dados.arquivo);
    } catch (erro) {
      alert("Erro: " + erro.message);
    } finally {
      setCarregando(false);
    }
  };

  return (
    <div className="App">
      <header>
        <h1>Downloader Youtube</h1>
      </header>
      <main>
        <div className="container">
          <div className="form">
            <form onSubmit={enviar}>
              <input
                type="text"
                name="url"
                placeholder="Insira o link do vídeo"
                onChange={(e) => setLink(e.target.value)}
                required
              />
              <button className='button-search' type="submit"><FontAwesomeIcon icon={faMagnifyingGlass} /></button>
            </form>

            {carregando && <p>Baixando vídeo... aguarde</p>}

            {dir && (
              <div className='box-thumb'>
                <img src={thumb} alt="thumbnail" width="300" />
                <div className='titulo-video'>{titulo}</div>
                <a
                  href={dir}
                  download={`${titulo}.mp4`}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  Clique aqui para baixar o vídeo
                </a>
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}

export default App;
