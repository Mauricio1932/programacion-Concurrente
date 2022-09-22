import requests
import time
import threading
import mysql.connector
from pytube import YouTube


# descargar 5 videos
# escribir en base de datos 2000 registros
# generar solicitud a ramdom user 50 usuarios dif.


# Escribir en Db
def get_pokemones():
    url = 'https://pokeapi.co/api/v2/pokemon?limit=10&offset=0'
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        results = data.get('results', [])
        if results:
            for x in results:
                name_pokemon = x['name']
                write_db(name_pokemon)

def write_db(name_pokemon):
    conexion = mysql.connector.connect(
        user='root',
        password='escapy1231',
        host='localhost',
        database='pokemon',
        port='3306'
    )

    cursor_conexion = conexion.cursor()
    sql = "INSERT INTO pokemones(namepokemon) VALUES ('{0}')".format(name_pokemon)
    cursor_conexion.execute(sql)
    conexion.commit()
    print("se agrego pkemon: " + name_pokemon )

# descarga videos
def descarga_videos():
    ruta_destino = ("C:/Users/alexm/Downloads/concurrente")
    ruta_video = ["https://youtu.be/lFw6sxMGIHk", "https://youtu.be/IQPhLCkUugw","https://youtu.be/enup62u1LEk", "https://youtu.be/B02yu8ih-C0", "https://youtu.be/yoWISASmVHw"]

    for link in ruta_video:
        yt = YouTube(link)
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first()
        carpeta_videos(video, ruta_destino)

def carpeta_videos(video, ruta_destino):
    video.download(ruta_destino)
    print("video descargado en: "+ruta_destino)

# Ramdom

def get_services(x=0):
    print(f'Data input = {x}')
    response = requests.get('https://randomuser.me/api/')
    time.sleep(0.2)
    if response.status_code == 200:
        results = response.json().get('results')
        name = results[0].get('name').get('first')
        print(name)


if __name__ == '__main__':
    for x in range(0, 50):
        th1 = threading.Thread(target=get_services, args=[x])
        th1.start()
    th2 = threading.Thread(target=descarga_videos)
    th2.start()
    th3 = threading.Thread(target=get_pokemones)
    th3.start()

    th1.join()
    th3.join()
    th3.join()
    # get_services()
