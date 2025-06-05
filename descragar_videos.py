import os
from pytube import YouTube

# URL del video
url = "https://www.youtube.com/watch?v=ophjWooCCiw"

# Carpeta de descargas del usuario
downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")

try:
    # Crear objeto YouTube
    yt = YouTube(url)

    # Seleccionar la mejor resolución disponible
    stream = yt.streams.get_highest_resolution()

    print(f"Descargando: {yt.title}...")
    stream.download(downloads_folder)
    print(f"Descarga completada en: {downloads_folder}")

except Exception as e:
    print("Error al descargar el video:", e)
