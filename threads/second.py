import requests
import time
import threading
import mysql.connector
from pytube import YouTube

# 5 subprocesos al mismo tiempo, descargar 5 videos, escribir en base de datos por lo menos 2000 registros, generar una solicitud a ramdon user por lo menos 50 usuarios

# def get_pokemones():

#     url = 'https://pokeapi.co/api/v2/pokemon?limit=2000&offset=0'
#     data = requests.get(url)
#     if data.status_code == 200:
#         data = data.json()
#         results = data.get('results', [])
#         if results:
#             for x in results:
#                 pokename = x['name']
#                 write_pokemones(pokename)

# def write_pokemones(pokename):
#     conexion = mysql.connector.connect(
#         user='root',
#         password='200116qw',
#         host='localhost',
#         database='pokemones',
#         port='3306'
#     )
#     mycursor = conexion.cursor()
#     sql = "INSERT INTO poke(pokename) VALUES ('{0}')".format(pokename)
#     mycursor.execute(sql)
#     conexion.commit()

# def download_video():
#     destino = ("C:/Users/Yurandier/OneDrive/Escritorio/python/videos")

#     urls_video = ["https://www.youtube.com/watch?v=3GQvsthnjeE",
#                   "https://www.youtube.com/watch?v=tIpzfs5tBJU",
#                   "https://www.youtube.com/watch?v=qcR1KbbhRTs",
#                   "https://www.youtube.com/watch?v=lYdXgHbnQX4",
#                   "https://www.youtube.com/watch?v=VuDc8HQ3Rbg"]

#     for link in urls_video:
#       yt = YouTube(link)
#       video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
#       save_video(video,destino)

# def save_video(video,destino):
#     video.download(destino)
#     print("Se ha descargado los videos"+destino)


def get_services():
    x = 0
    for x in range(0, 50):
        print(f'Data input = {x}')
        response = requests.get('https://randomuser.me/api/')
        time.sleep(0.3)
        if response.status_code == 200:
            results = response.json().get('results')
            name = results[0].get('name').get('first')
            print(name)


if __name__ == '__main__':
    th1 = threading.Thread(target=get_services)
    # th2 = threading.Thread(target=download_video)
    # th3 = threading.Thread(target=get_pokemones)

    th1.start()
    # th2.start()
    # th3.start()

    # th1.join()
    # th2.join()
    # th3.join()
    print("El programa a finalizado")
