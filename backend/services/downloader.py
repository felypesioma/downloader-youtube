from pytubefix import YouTube
import re
import os
import unicodedata

def mostrar_progresso(stream, pedaco, restante):
    total = stream.filesize
    baixado = total - restante
    porcentagem = (baixado / total) * 100
    print(f"Progresso: {porcentagem:.2f}%")

def limpar_nome(nome):
    # Remove acentos
    nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('utf-8')
    # Substitui espaços e hífens por underline
    nome = nome.replace(' ', '_').replace('-', '_')
    # Remove tudo que não for letra, número ou underline
    nome = re.sub(r'[^a-zA-Z0-9_]', '', nome)
    return nome

def baixar_video(link):
    pasta_destino = "frontend/src/pasta_videos"
    os.makedirs(pasta_destino, exist_ok=True)

    video = YouTube(link, on_progress_callback=mostrar_progresso)
    titulo = video.title
    print(f"Baixando: {titulo}")
    stream = video.streams.get_highest_resolution()
    thumb = video.thumbnail_url
    print("Thumbnail:", thumb)

    titulo_limpo = limpar_nome(titulo)
    arquivo = titulo_limpo + ".mp4"

    stream.download(output_path=pasta_destino, filename=arquivo)

    print("Download finalizado")
    print("Arquivo salvo como:", arquivo)
    print("Servindo da pasta:", pasta_destino)
    return arquivo, thumb, titulo
