from threading import Thread
import threading 
import time, random
import queue

almacen = queue.Queue(maxsize=20)

class Productor(Thread):
    def __init__(self, array1):
        threading.Thread.__init__(self)
        self.array1 = array1

    def run(self):
        while True:
            if not almacen.full():
                array1 = random.randint(0, 20)
                almacen.put(array1)
                print("Se agrego un nuevo intem: " + str(array1))
                time.sleep(3)

class Consumidor(Thread):
    def __init__(self,array2):
        threading.Thread.__init__(self)
        self.array = array2

    def run(self):
        while True:
            if not almacen.empty():
                array2 = almacen.get()
                print('El Consumidor tomo el producto: '+str(array2))
                time.sleep(3)

def main():
    array=[]
    hilo_produtor = Productor(array)
    hilo_consumidor = Consumidor(array)

    hilo_produtor.start()
    hilo_consumidor.start()

main()