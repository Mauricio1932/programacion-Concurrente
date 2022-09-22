import threading
import time
import json
import requests
import mysql.connector
from unittest import result

import concurrent.futures


threading_local = threading.local();

# Implementar requests
# consumir un servicio que descarge por lo menos 5000 registros
# utilizar un for
# for x in data:
# write_db(x.name)

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, url)
    
def get_service(url):
    data = requests.get(url)
    if data.status_code == 200:
        data = data.json()
        results = data.get('results', [])
        if results:
            for x in results:
                namepokemon = x['name']
                connection(namepokemon)

def connection(namepokemon):
    conexion = mysql.connector.connect(
        user='root',
        password='escapy1231',
        host='localhost',
        database='pokemon',
        port='3306'
    )
    write_db(conexion, namepokemon)


def write_db(conexion,namepokemon):
    mycursor = conexion.cursor()
    sql = "INSERT INTO pokemones(namepokemon) VALUES ('{0}')".format(namepokemon)
    mycursor.execute(sql)
    conexion.commit()

if __name__ == "__main__":
    url = ['https://pokeapi.co/api/v2/pokemon?limit=2308&offset=0']
    init_time  = time.time();
    service(url)
    end_time = time.time() - init_time
    print(end_time)