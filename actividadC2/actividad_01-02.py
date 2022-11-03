#Programa Restaurante
#Mauricio Alejandro Ocampo Lopez 201227
#Jesus Eduardo Jimenez Guillen 201258

from threading import Thread 
import queue, time
import threading 
import random

colaM = queue.Queue(maxsize=20)


colaRestaurante2 = queue.Queue(maxsize=20)
colaRestaurante = queue.Queue(maxsize=20)
mutex = threading.Lock()
Ordenes = queue.Queue()   
cocinero = queue.Queue()

PERSONAS = 20

cantidad = float(10)
mesero = int(cantidad * colaRestaurante2.maxsize/100)
meseros = queue.Queue(maxsize=mesero)

class Persona(threading.Thread):
    def __init__(self, id, monitor):
        threading.Thread.__init__(self)
        self.id= id
        self.monitor = monitor

    def reserva(self):
        flotante = float(20)
        recepcion = int(flotante * colaM.maxsize/100)
        if not colaM.full():
            for x in range(recepcion):
                colaM.put(self.id)
                print("Reservacion Para"+ str(self.id+1))
                self.atencion()
                self.monitor.wait()
        else:
            self.atencion()

    def espera(self):
        ciclo = True
        with self.monitor:
                    if colaRestaurante.full():
                        print("Cliente Esperando: "+str(self.id+1))
                        time.sleep(3)
                        self.monitor.wait()
                        if not colaRestaurante.empty():
                            self.ingreso()
                    else:
                        self.ingreso()   


    def entregar(self):
        with self.monitor:
            while not cocinero.empty():
                        cocinero.get(self.id)
                        print("El mesero sirve la comida al cliente "+str(self.id+1))
                        colaRestaurante.put(self.id)
                        self.cenando()
                        self.monitor.wait()

    def cenando(self):
        with self.monitor:
            if not cocinero.full():
                print("cliente: "+str(self.id+1)+" cenando")
                time.sleep(random.randint(2, 6))
                print("cliente: "+str(self.id+1)+" Satisfecho")
                colaRestaurante.get(self.id)
                self.monitor.wait()
            else:
                self.espera()  

    
    def cocina (self):
        ciclo = True
        with self.monitor:
            while not Ordenes.empty():
                    if not cocinero.full():
                        Ordenes.get(self.id)
                        print("Cocinero prepara la comida para cliente: "+str(self.id+1))
                        time.sleep(4)
                        cocinero.put(self.id)
                        self.monitor.wait()
                        self.entregar()
                    else:
                        self.ordenar()
                        self.espera()   


    def ordenar(self):
        cant = float(10)
        mesero = int(cant * colaRestaurante2.maxsize/100)
        meseros = queue.Queue(maxsize=mesero)
        ciclo = True
        with self.monitor:
            while not colaRestaurante2.empty():
                    if not Ordenes.full():
                        colaRestaurante2.get(self.id)
                        for x in range(meseros.maxsize):
                            print("Mesero anotando la orden del cliente: "+str(self.id+1))
                            time.sleep(5)
                            Ordenes.put(self.id)
                            self.monitor.notify()
                            self.cocina()
                    else:
                        self.cocina()                     
    def atencion(self):
        
        while  not colaM.empty():
            if not colaRestaurante2.full():     
                colaM.get(self.id)
                print("atencion cliente:" + str(self.id+1))
                time.sleep(5)
                colaRestaurante2.put(self.id)
                print("Cliente: " +str(self.id+1)+ " ha entrado al restaurante")
                time.sleep(5)
                self.ordenar()
                self.monitor.notify()
                    
            else:
                self.reserva()
                self.ordenar()
    
    def ingreso(self):
        ciclo = True
        if not colaM.full():
            colaM.put(self.id)
            print("nuevo cliente: " + str(self.id+1))
            self.atencion()
            self.reserva()
        else:
            self.espera()
            self.reserva()
    def run(self):
        self.ingreso()
        self.reserva()
        self.atencion()
        self.ordenar()
        self.cocina()
        self.entregar()

monitoreo = threading.Condition()           
recepcionista = [1]   
def main():
    personas = []

    for i in range(PERSONAS):
        personas.append(Persona(i,monitoreo))

    for p in personas:
        p.start()
    
    for p in personas:
        p.join()

if __name__ == "__main__":
    main()