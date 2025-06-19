import pygame
import random
import sys

from pyrect import HEIGHT

pygame.init()

WIDTH, HEIGHT = 400,300
window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Haz click en el circulo')

RED=(255,0,0)
WHITE =(255,255,255)
BLACK= (0,0,0,)

circulo_radies = 20
circulo_x = random.randint(circulo_radies, WIDTH - circulo_radies)
circle_y = random.randint(circulo_radies,HEIGHT - circulo_radies)

score = 0
font = pygame.font.Font(None,36)


while True:
    window.fill(WHITE)

    pygame.draw.circle(window,RED,(circulo_x,circle_y),circulo_radies)
    score_text = font.render(f'Puntos:{score}',True,BLACK)
    window.blit(score_text,(10,10))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = event.pos
            if (mouse_x - circulo_x) **2 +(mouse_y - circle_y) **2 < circulo_radies **2:
                circulo_x = random.randint(circulo_radies, WIDTH - circulo_radies)
                circle_y = random.randint(circulo_radies, HEIGHT - circulo_radies)
                score +=1


