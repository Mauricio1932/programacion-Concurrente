import threading
from pytube import YouTube

mutex = threading.Lock()

def descarga(vid):
    yt = YouTube(vid)
    video=  yt.streams.filter(file_extension='mp4').order_by('resolution').first()
    video.download(destino)
    print("video descargado en: "+destino)

class Hilo(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        video=id
        self.id=video


    def run(self):
        mutex.acquire()
        descarga(self.id)
        mutex.release()

destino=r"C:/Users/alexm/Downloads/descargas_python"

Hilos = [Hilo('https://youtu.be/B02yu8ih-C0'), Hilo('https://youtu.be/enup62u1LEk'), Hilo('https://youtu.be/IQPhLCkUugw'), Hilo('https://youtu.be/lFw6sxMGIHk'),
Hilo('https://youtu.be/p5709BE-fR8'), Hilo('https://youtu.be/YMkGOwosPgw'), Hilo('https://youtu.be/geg3CsgXC8Q'), Hilo('https://youtu.be/sZpJ_4lj0y8'), Hilo('https://youtu.be/yoWISASmVHw'),
Hilo('https://youtu.be/ETa2xOLFzeM')]


for h in Hilos:
    h.start()