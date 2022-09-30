import argparse
import threading
import time
import random

estado_persona = None

candados = []
cantidad_personas = 0
velocidad_comer = 0
TOTAL_TIEMPO_COMER = 0

estado_espera = "F"
ESTADO_COMIENDO = "C"


def tomar_palillo(num_persona):

    palillo_izquierdo = candados[num_persona]
    palillo_derercho = candados[(num_persona - 1) % cantidad_personas]

    palillo_izquierdo.acquire()

    if palillo_derercho.acquire(blocking=False):
        return True
    else:
        palillo_izquierdo.release()
        return False


def soltar_palillo(num_persona):
    candados[num_persona].release()
    candados[(num_persona - 1) % cantidad_personas].release()


def iniciar_comer(num_persona):

    intentos_fallidos = 0
    tiempo_comiendo = 0

    while tiempo_comiendo < TOTAL_TIEMPO_COMER:
        if tomar_palillo(num_persona):
            intentos_fallidos = 0

            tiempo_comer = min(
                velocidad_comer, TOTAL_TIEMPO_COMER - tiempo_comiendo)
            tiempo_comiendo += tiempo_comer
            print(f"persona {num_persona} comiendo, {tiempo_comer} seg.")
            time.sleep(tiempo_comiendo)
            soltar_palillo(num_persona)

            estado_persona[num_persona] = estado_espera

            tiempo_esperando = random.uniform(0, 5)
            print(
                f"persona {num_persona} esperando, {tiempo_esperando:.2f} seg.")
            time.sleep(tiempo_esperando)
        else:
            estado_persona[num_persona] = estado_espera

            intentos_fallidos += 1

            tiempo_reintentar = random.uniform(0, 3)
            print(f"persona {num_persona} intenta tomar palillo", f" Intento {intentos_fallidos}, tiempo {tiempo_reintentar:.2f} seg.")
            time.sleep(tiempo_reintentar)


def asignar_argumentos():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num_personas", type=int,default=8, help="Número de personas (hilos)")
    parser.add_argument("-r", "--velocidad_comer", type=int,default=4, help="velocidad en comer de los personas")
    parser.add_argument("-t", "--tiempo_total", type=int,default=10, help="Tiempo para liberar el palillo")
    return parser.parse_args()


if __name__ == '__main__':
    args = asignar_argumentos()

    cantidad_personas = args.num_personas
    velocidad_comer = args.velocidad_comer
    TOTAL_TIEMPO_COMER = args.tiempo_total

    estado_persona = cantidad_personas * [estado_espera]

    for _ in range(cantidad_personas):
        candados.append(threading.RLock())

    hilos = []
    for i in range(args.num_personas):
        nuevo_hilo = threading.Thread(target=iniciar_comer, args=(i,))
        hilos.append(nuevo_hilo)

    for hilo in hilos:
        hilo.start()

    for hilo in hilos:
        hilo.join()
