from pytubefix import YouTube
import re
import os

def mostrar_progresso(stream, pedaco, restante):
    total = stream.filesize
    baixado = total - restante
    porcentagem = (baixado / total) * 100
    print(f"Progresso: {porcentagem:.2f}%")

def baixar_video(link):
    pasta_destino = "pasta_videos"
    os.makedirs(pasta_destino, exist_ok=True)


    video = YouTube(link, on_progress_callback=mostrar_progresso)
    titulo = video.title
    print(f"Baixando: {titulo}")
    stream = video.streams.get_highest_resolution()
    thumb = video.thumbnail_url
    print(thumb)
    titulof = re.sub(r'["!., "]', '_', titulo)
    arquivo = titulof + ".mp4"
    stream.download(output_path=pasta_destino, filename=arquivo)
    print("Download finalizado")

    return arquivo, thumb
