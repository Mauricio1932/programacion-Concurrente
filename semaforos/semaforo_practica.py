from threading import Thread, Semaphore
from pytube import YouTube
semaforo = Semaphore(1)



def descarga(video):
    yt = YouTube(video)
    video=  yt.streams.filter(file_extension='mp4').order_by('resolution').first()
    video.download(destino)
    print("video descargado en: "+destino)

class Hilo(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        video=id
        self.id=video

    def run(self):
        semaforo.acquire()
        descarga(self.id)
        semaforo.release()


destino=r"C:/Users/alexm/Downloads/descargas_python"

threads_semaphore = [Hilo('https://youtu.be/B02yu8ih-C0'), Hilo('https://youtu.be/enup62u1LEk'), Hilo('https://youtu.be/IQPhLCkUugw'), Hilo('https://youtu.be/lFw6sxMGIHk'),
Hilo('https://youtu.be/p5709BE-fR8'), Hilo('https://youtu.be/YMkGOwosPgw'), Hilo('https://youtu.be/geg3CsgXC8Q'), Hilo('https://youtu.be/sZpJ_4lj0y8'), Hilo('https://youtu.be/yoWISASmVHw'),
Hilo('https://youtu.be/ETa2xOLFzeM')]

for t in threads_semaphore:
    t.start()