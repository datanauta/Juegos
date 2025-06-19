import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Tamaño de la pantalla y colores
WIDTH, HEIGHT = 500, 500
CELL_SIZE = 10
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Crear pantalla y reloj
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake")
clock = pygame.time.Clock()

# Función para generar comida en posición aleatoria
def generate_food():
    return [random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE,
            random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE]

# Función principal del juego
def main():
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50]]
    direction = "RIGHT"
    change_to = direction

    food_pos = generate_food()
    score = 0
    speed = 15

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Cambiar dirección con teclas
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"

        direction = change_to

        # Mover la serpiente
        if direction == "UP":
            snake_pos[1] -= CELL_SIZE
        elif direction == "DOWN":
            snake_pos[1] += CELL_SIZE
        elif direction == "LEFT":
            snake_pos[0] -= CELL_SIZE
        elif direction == "RIGHT":
            snake_pos[0] += CELL_SIZE

        # Añadir nueva cabeza a la serpiente
        snake_body.insert(0, list(snake_pos))

        # Comer comida
        if snake_pos == food_pos:
            score += 1
            food_pos = generate_food()
        else:
            snake_body.pop()

        # Comprobar colisión con bordes
        if (snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
            snake_pos[1] < 0 or snake_pos[1] >= HEIGHT):
            print("💀 Has chocado con el borde. Puntuación:", score)
            break

        # Comprobar colisión con sí misma
        if snake_pos in snake_body[1:]:
            print("💀 Te comiste a ti mismo. Puntuación:", score)
            break

        # Dibujar fondo, serpiente y comida
        screen.fill(BLACK)
        for segment in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], CELL_SIZE, CELL_SIZE))

        pygame.display.update()
        clock.tick(speed)

    pygame.quit()
    sys.exit()

# Ejecutar el juego
if __name__ == '__main__':
    main()

