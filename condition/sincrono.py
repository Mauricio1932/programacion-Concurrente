import time
import json
import requests
import mysql.connector
from unittest import result

# Implementar requests
# consumir un servicio que descarge por lo menos 5000 registros
# utilizar un for
# for x in data:
# write_db(x.name)


def get_service():
    urlPoke = 'https://pokeapi.co/api/v2/pokemon?limit=2308&offset=0'
    data = requests.get(urlPoke)
    if data.status_code == 200:
        data = data.json()
        results = data.get('results', [])
        if results:
            for x in results:
                namepokemon = x['name']
                write_db(namepokemon)


def write_db(namepokemon):
    conexion = mysql.connector.connect(
        user='root',
        password='escapy1231',
        host='localhost',
        database='pokemon',
        port='3306'
    )
    mycursor = conexion.cursor()
    sql = "INSERT INTO pokemones(namepokemon) VALUES ('{0}')".format(
        namepokemon)
    mycursor.execute(sql)
    conexion.commit()


if __name__ == "__main__":
    init_time = time.time()
    get_service()
    end_time = time.time() - init_time
    print(end_time)
