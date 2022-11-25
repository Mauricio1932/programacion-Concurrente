import pygame
import os
	
python = pygame.image.load(os.path.join('images', 'javaScript.png'))
js = pygame.image.load(os.path.join('images', 'python.png'))

pygame.init()
font = pygame.font.Font(None, 30)


# Clas para dibuja lineas
class Cuadro:
    def __init__(self):
        self.linea_cuadro = [
            ((0, 100), (300, 100)),  # primer linea horizontal
            ((0, 200), (300, 200)),  # segunda linea horizontal
            ((100, 0), (100, 300)),  # primer linea vertical
            ((200, 0), (200, 300)),  # segunda line vertical
        ]

        self.cuadro = [[0 for x in range(3)] for y in range(3)]
        # Buscar Direcciones  Norte   Noroeste   noeste    sur   Sureste   Sureste      Este       Noreste
        self.direccion_busqueda = [ (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0),    (1, -1)]
        self.switch_player = True
        self.game_over = False

    # metodo para dibujar
    def dibujar(self, superficie, segundos):
        
        text = str(segundos)
        mensaje = font.render(text, 1, (255, 255, 255))
        for line in self.linea_cuadro:
            print(segundos)
            # dibjuja las lineas del tablero
            pygame.draw.line(superficie, (200, 200, 200), line[0], line[1], 2)
            # superficie.blit(mensaje, (40,40))
        for y in range(len(self.cuadro)):
            for x in range(len(self.cuadro[y])):
                # valida que que jugador esta en turno para dibjuar en su repectivo cuadro
                if self.obtener_celda_valor(x, y) == "X":
                    superficie.blit(python, (x * 100, y * 100))
                elif self.obtener_celda_valor(x, y) == "O":
                    superficie.blit(js, (x * 100, y * 100))    
                superficie.blit(mensaje, (40,40))

    def obtener_celda_valor(self, x, y):
        return self.cuadro[y][x]

    def set_celda_valor(self, x, y, value):
        self.cuadro[y][x] = value

    def get_mouse(self, x, y, player):
        # Compara que la selda no se halla ocupado
        if self.obtener_celda_valor(x, y) == 0:
            # self.switch_player = True  # Vuelve a verdadero que no se a ocupado la misma celda
            self.set_celda_valor(x,y,player) #llena el cuadro del jugador
            self.check_grid(x, y, player)

    def imprimir_cuadro(self):
        for row in self.cuadro:
            print(row)

    def posicion_valida(self, x, y):
        return x >= 0 and x < 3 and y >= 0 and y < 3

    def check_grid(self, x, y, player):
        count = 1
        for index, (dirx, diry) in enumerate(self.direccion_busqueda): #busca las posiciones del tablero retonda indece y valor dentro 
            if self.posicion_valida(x+dirx, y+diry) and self.obtener_celda_valor(x+dirx, y+diry) == player: #valida la pocicion se valida y obtine el valor de la celda
                count += 1
                xx = x + dirx
                yy = y + diry
                if self.posicion_valida(xx+dirx, yy+diry) and self.obtener_celda_valor(xx+dirx, yy+diry) == player:
                    count += 1
                    if count == 3:
                        break
                if count < 3:
                    new_dir = 0
                    # 74 / 5.000 Resultados de traducción asignando los índices a la dirección opuesta: 0-4 1-5 2-6 3-7 4-0 5-1 6-2 7-3
                    if index == 0:
                        new_dir = self.direccion_busqueda[4]  # N a S
                    elif index == 1:
                        new_dir = self.direccion_busqueda[5]  #noroeste a suroeste
                    elif index == 2:
                        new_dir = self.direccion_busqueda[6]  # W a Este
                    elif index == 3:
                        new_dir = self.direccion_busqueda[7]  # suroeste a noroeste
                    elif index == 4:
                        new_dir = self.direccion_busqueda[0]  # Sur a Norte
                    elif index == 5:
                        new_dir = self.direccion_busqueda[1]  # suroeste a noroeste
                    elif index == 6:
                        new_dir = self.direccion_busqueda[2]  # Este a oeste
                    elif index == 7:
                        new_dir = self.direccion_busqueda[3]  # NE a suroeste

                    if self.posicion_valida(x + new_dir[0], y + new_dir[1]) \
                            and self.obtener_celda_valor(x + new_dir[0], y + new_dir[1]) == player:
                        count += 1
                        if count == 3:
                            break
                    else:
                        count = 1

        if count == 3:
            print(player, 'wins!')
            self.game_over = True
        else:
            self.game_over = self.cuadro_lleno()

    def cuadro_lleno(self):
        for row in self.cuadro:
            for value in row:
                if value == 0:
                    return False
        return True


    def limpiar_cuadro(self): #metodo para restablecer el tablero
        for y in range(len(self.cuadro)):
            for x in range(len(self.cuadro[y])):
                self.set_celda_valor(x, y, 0)

    def print_grid(self):
        for row in self.grid:
            print(row)