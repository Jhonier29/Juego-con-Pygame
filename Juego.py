import pygame
import sys
import random
import math

pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esquivar Enemigos")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)

# Clase para el jugador
class Jugador:
    def __init__(self):
        self.radio = 20
        self.x, self.y = ANCHO // 2, ALTO // 2
        self.velocidad = 5
        self.puntuacion = 0

    def dibujar(self):
        pygame.draw.circle(pantalla, BLANCO, (self.x, self.y), self.radio)

    def actualizar(self, mouse_x, mouse_y):
        self.x = mouse_x
        self.y = mouse_y

# Clase para los enemigos
class Enemigo:
    def __init__(self):
        self.ancho = 40
        self.alto = 40
        self.x = random.randint(0, ANCHO - self.ancho)
        self.y = random.randint(0, ALTO - self.alto)
        self.velocidad_x = random.uniform(-1, 1)
        self.velocidad_y = random.uniform(-1, 1)

    def dibujar(self):
        pygame.draw.rect(pantalla, ROJO, pygame.Rect(self.x, self.y, self.ancho, self.alto))

    def mover(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y

        max_velocidad = 3
        if self.velocidad_x > max_velocidad:
            self.velocidad_x = max_velocidad
        if self.velocidad_y > max_velocidad:
            self.velocidad_y = max_velocidad

        if self.x < 0 or self.x + self.ancho > ANCHO:
            self.velocidad_x *= -1.5
        if self.y < 0 or self.y + self.alto > ALTO:
            self.velocidad_y *= -1.5

# Clase para los triángulos
class Triangulo:
    def __init__(self):
        self.lado = 40
        self.x = random.randint(0, ANCHO - self.lado)
        self.y = random.randint(0, ALTO - self.lado)

    def dibujar(self):
        pygame.draw.polygon(pantalla, VERDE, [(self.x, self.y), (self.x + self.lado, self.y), (self.x + self.lado / 2, self.y + (self.lado * math.sqrt(3) / 2))])

# Función para mostrar texto en pantalla
def mostrar_texto(texto, x, y, color, fuente, tamaño):
    font = pygame.font.Font(fuente, tamaño)
    texto_surface = font.render(texto, True, color)
    pantalla.blit(texto_surface, (x, y))

# Función para mostrar el menú de inicio
def mostrar_menu():
    mostrar_texto("Esquivar Enemigos", ANCHO // 2 - 150, ALTO // 2 - 50, BLANCO, None, 36)
    mostrar_texto("Haz clic en los triángulos y esquiva cuadrados.", ANCHO // 2 - 250, ALTO // 2, BLANCO, None, 36)
    mostrar_texto("Haz clic para empezar.", ANCHO // 2 - 100, ALTO // 2 + 50, BLANCO, None, 36)
    mostrar_texto("Tu última puntuación es", ANCHO // 2 - 200, ALTO // 2 + 150, ROJO, None, 36)
    mostrar_texto(str(jugador.puntuacion), ANCHO // 2 + 100, ALTO // 2 + 150, ROJO, None, 36)

# Función para mostrar la pantalla de pérdida
def mostrar_pantalla_perdida():
    mostrar_texto("¡Has perdido!", ANCHO // 2 - 100, ALTO // 2 - 50, ROJO, None, 36)
    mostrar_texto(f"Puntuación: {jugador.puntuacion}", ANCHO // 2 - 75, ALTO // 2, ROJO, None, 36)
    mostrar_texto("Haz clic para continuar", ANCHO // 2 - 100, ALTO // 2 + 50, ROJO, None, 36)

# Inicialización del jugador
jugador = Jugador()

# Listas para enemigos y triángulos
enemigos = []
triangulos = []

# Estado del juego
en_menu = True
jugando = False
pantalla_perdida = False

# Bucle principal del juego
RELOJ = pygame.time.Clock()
ejecutando = True

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        # Evento que se activa cuando se da click con el mouse
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if en_menu:
                en_menu = False
                jugando = True
                jugador.puntuacion = 0
            elif jugando:
                for triangulo in triangulos:
                    # Comprueba si se hizo clic en un triángulo
                    if (
                        jugador.x < 20 + triangulo.x + triangulo.lado / 2
                        and jugador.x + jugador.radio > triangulo.x
                        and jugador.y < triangulo.y + (triangulo.lado * math.sqrt(3) / 2)
                        and jugador.y + jugador.radio > triangulo.y
                    ):
                        triangulos.remove(triangulo)
                        jugador.puntuacion += 5
                        triangulos.append(Triangulo())
                for enemigo in enemigos:
                    # Comprueba si el jugador colisiono con un cuadrado
                    if (
                        jugador.x < enemigo.x + enemigo.ancho
                        and jugador.x + jugador.radio > enemigo.x
                        and jugador.y < enemigo.y + enemigo.alto
                        and jugador.y + jugador.radio > enemigo.y
                    ):
                        jugando = False
                        pantalla_perdida = True
            elif pantalla_perdida:
                # Reinicia el juego cuando se hace clic después de perder
                enemigos = []
                triangulos = []
                pantalla_perdida = False
                en_menu = True

    pantalla.fill((0, 0, 0))

    if en_menu:
        mostrar_menu()
    elif jugando:
        jugador.actualizar(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        jugador.dibujar()

        if len(enemigos) < 10:
            enemigos.append(Enemigo())
        if len(triangulos) < 1:
            triangulos.append(Triangulo())

        for enemigo in enemigos:
            enemigo.mover()
            enemigo.dibujar()

        for triangulo in triangulos:
            triangulo.dibujar()

        fuente = pygame.font.Font(None, 36)
        texto_puntuacion = fuente.render(f"Puntuación: {jugador.puntuacion}", True, BLANCO)
        pantalla.blit(texto_puntuacion, (10, 10))

        for enemigo in enemigos:
            if (
                jugador.x < enemigo.x + enemigo.ancho
                and jugador.x + jugador.radio > enemigo.x
                and jugador.y < enemigo.y + enemigo.alto
                and jugador.y + jugador.radio > enemigo.y
            ):
                jugando = False
                pantalla_perdida = True

    elif pantalla_perdida:
        mostrar_pantalla_perdida()

    pygame.display.update()
    RELOJ.tick(60)

pygame.quit()
sys.exit()