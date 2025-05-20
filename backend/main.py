from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from services import downloader
import os

app = Flask(__name__)
CORS(app)

@app.route("/download", methods=["POST"])
def download_videos():
    dados = request.get_json()
    if not dados or "link" not in dados:
        return jsonify({"Erro": "Link faltando"})

    arquivo, urlt, titulo = downloader.baixar_video(dados["link"])
    return jsonify({
        "arquivo": arquivo,
        "thumb": urlt,
        "titulo": titulo
    })

@app.route('/pasta_videos/<path:filename>')
def download_file(filename):
    pasta = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend', 'src', 'pasta_videos'))
    print("Servindo da pasta:", pasta)
    print("Arquivo solicitado:", filename)
    return send_from_directory(pasta, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
