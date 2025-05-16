from flask import Flask, jsonify, request
from flask_cors import CORS
from services import downloader

app = Flask(__name__)

@app.route("/api/downloader", methods=["POST"])
def download_videos():

    dados = request.get_json()
    if not dados or "link" not in dados:
        return jsonify({"Erro": "Link faltando"})

    titulo, urlt = downloader.baixar_video(dados["link"])
    return jsonify({
        "titulo": titulo,
        "thumb": urlt
    })

if __name__ == "__main__":
    app.run(debug=True)