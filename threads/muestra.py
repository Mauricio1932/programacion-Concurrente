import requests
import concurrent.futures
import threading
import time

threading_local = threading.local()

# Investigar sobre la libreria threading en python

def service(url):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(get_service, url)

def get_service(url):
    print(url)
    # print("Consume servicio")
    connection_db()
    # Implementar requests
    # Consumir un servicio que descarge por lo menos 5000 registros 

def connection_db():
    write_db()
    print("Conecta a la base de datos")

def write_db():
    print("Escribre en la base de datos")
    # Escribir el response en una base de datos

if __name__ == "__main__":
    url_site = ['url']
    init_time = time.time()
    service(url_site)
    end_time = time.time() - init_time
    print(end_time)