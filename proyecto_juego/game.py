#Mauricio Alejandro Ocampo Lopez 201227
#Jesus Eduardo Jimenez Guillen 201258
# hoja de servidor
import pygame
import socket
import threading
import time

from cuadro import Cuadro

superficie = pygame.display.set_mode((300, 300))  # ventana de juego
pygame.display.set_caption('Proyecto Jugador 1')


cuadro = Cuadro()  # instancia del met constructor de la clase

rungame = True  # bolean para mantener el juego en ejcucion
player = "X"  # jugador que inicia el juego
turno = True
jugando = 'True'
segundos = 0
seg = "0"
# variables de conexion
HOST = '127.0.0.1'
PORT = 8000
conexion_establecida = False
conn, addr = None, None

#                       protolo IPv4          redes TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Metodo que vincula y escuchar las solicitudes entrantes en esa IP y puerto
sock.bind((HOST, PORT))
sock.listen(1)  # Metodo de escucha para un numero conexiones


def recibir_datos():
    global turno
    while True:
        data = conn.recv(1024).decode()
        data = data.split('-')
        x, y = int(data[0]), int(data[1])
        if data[2] == 'tu_turno':
            turno = True
        if data[3] == 'False':
            cuadro.game_over = True
        if cuadro.obtener_celda_valor(x,y) == 0: #valoramos que la celda este libre (no ocupado)
            cuadro.set_celda_valor(x,y,'O') #Cambiamos el valor al jugador en turno
        print(data)


def crear_hilo(target):
    thread = threading.Thread(target=target)
    thread.daemon = True  # Subproceso para seguir en segundo plano
    thread.start()  # se inicia la ejecucion del subproceso


def espera_conexion():
    # variable global
    global conn, addr, conexion_establecida
    conn, addr = sock.accept()  # espera una conexion, y es un bloqueo
    print('conexion establecida')
    conexion_establecida = True
    recibir_datos()

def cronometro():
    global seg, segundos
    while rungame:
        time.sleep(1)
        segundos += 1
        seg = str(segundos)
        # print(seg)

crear_hilo(espera_conexion)
crear_hilo(cronometro)

while rungame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rungame = False

        if event.type == pygame.MOUSEBUTTONDOWN and conexion_establecida:  # evento de presiona el boton
            # evalua que el boton del mouse sea el derecho
            if pygame.mouse.get_pressed()[0]:
                if turno and not cuadro.game_over:
                    posicion = pygame.mouse.get_pos()  # obtinene su posicion
                    # print (posicion[0] // 100 , posicion[1] // 100) #poscion de los cuadro del tablero
                    celda_x, celda_y = posicion[0] // 100, posicion[1] // 100
                    # metodo para ver tabla de juego
                    cuadro.get_mouse(celda_x, celda_y, player)
                    if cuadro.game_over:
                        jugando = 'False'
                    enviar_datos = '{}-{}-{}-{}'.format(celda_x, celda_y, 'tu_turno', jugando).encode()
                    conn.send(enviar_datos)
                    turno = False

        if event.type == pygame.KEYDOWN:
            # valida que la tecla pres sea espacio y que el juego se encutre en un estado terminado
            if event.key == pygame.K_SPACE and cuadro.game_over:
                cuadro.limpiar_cuadro()  # limpiamos el tablero
                cuadro.game_over = False  # Restablecemos la variable de juego
                jugando = 'True'
            elif event.key == pygame.K_ESCAPE:
                rungame = False

    superficie.fill((50, 50, 50))
    # llamada del metodo dibujar, solo pasamos el ancho del display
    cuadro.dibujar(superficie,seg)
    pygame.display.flip()
