import pygame
import random
import sys

pygame.init()

# Tamaño de pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Papá Noel sin imágenes')

# Colores
COLOR_FONDO = (10, 10, 50)          # Azul oscuro
COLOR_SANTA = (255, 0, 0)           # Rojo
COLOR_REGALO = (0, 255, 0)          # Verde
COLOR_TEXTO = (255, 255, 255)       # Blanco

# Tamaño de "Santa" y regalos
santa_w, santa_h = 80, 80
regalo_w, regalo_h = 50, 50

# Posición inicial de Santa
santa_x = ANCHO // 2
santa_y = ALTO - santa_h - 10
velocidad = 10

# Lista de regalos
regalos = []
for _ in range(5):
    x = random.randint(0, ANCHO - regalo_w)
    y = random.randint(-600, -50)
    regalos.append([x, y])

# Reloj y fuente
reloj = pygame.time.Clock()
fuente = pygame.font.SysFont(None, 36)
puntos = 0

def mostrar_puntaje(puntaje):
    texto = fuente.render(f'Puntos: {puntaje}', True, COLOR_TEXTO)
    pantalla.blit(texto, (10, 10))

# Bucle principal del juego
while True:
    pantalla.fill(COLOR_FONDO)

    # Dibujar a Santa (rectángulo rojo)
    santa_rect = pygame.Rect(santa_x, santa_y, santa_w, santa_h)
    pygame.draw.rect(pantalla, COLOR_SANTA, santa_rect)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento de Santa
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and santa_x > 0:
        santa_x -= velocidad
    if teclas[pygame.K_RIGHT] and santa_x < ANCHO - santa_w:
        santa_x += velocidad

    # Mover y dibujar regalos (rectángulos verdes)
    for regalo in regalos:
        regalo[1] += 5
        regalo_rect = pygame.Rect(regalo[0], regalo[1], regalo_w, regalo_h)
        pygame.draw.rect(pantalla, COLOR_REGALO, regalo_rect)

        # Verificar colisión
        if santa_rect.colliderect(regalo_rect):
            puntos += 1
            regalo[0] = random.randint(0, ANCHO - regalo_w)
            regalo[1] = random.randint(-600, -50)

        # Reiniciar si se cae
        if regalo[1] > ALTO:
            regalo[1] = random.randint(-600, -50)
            regalo[0] = random.randint(0, ANCHO - regalo_w)

    # Mostrar puntos
    mostrar_puntaje(puntos)

    pygame.display.flip()
    reloj.tick(60)
