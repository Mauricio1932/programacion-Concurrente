import time
import threading
import concurrent.futures
from pytube import YouTube

threading_local = threading.local()


def service(destino):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_video, destino)


def download_video(destino):
    urls_video = ["https://youtu.be/lFw6sxMGIHk", "https://youtu.be/IQPhLCkUugw", "https://youtu.be/enup62u1LEk", "https://youtu.be/B02yu8ih-C0", "https://youtu.be/yoWISASmVHw"]
    for link in urls_video:
        yt = YouTube(link)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first()
        save_video(video, destino)


def save_video(video, destino):
    video.download(destino)
    print("Se ha descargado los videos"+destino)


if __name__ == "__main__":
    init_time = time.time()
    destino = ["C:/Users/alexm/Downloads/concurrente"]
    service(destino)
    end_time = time.time()-init_time 
    print(end_time)
