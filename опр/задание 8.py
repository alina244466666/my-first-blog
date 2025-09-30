from itertools import count

import pygame
from pygame.color import THECOLORS

pygame.init()
dis = pygame.display.set_mode((400,400))
pygame.display.set_caption
dis.fill(THECOLORS['gray'])

font = pygame.font.SysFont('couriernew', 20)
r = pygame.Rect(100, 100, 100, 100)

dis_over = False
while not dis_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dis_over = True
            pygame.quit()
    count=0
    for x in range(10, 400, 40):
        for y in range(1, 400, 40):
            pygame.draw.rect(dis,THECOLORS['lightgreen'] , (x, y, 40, 40), 5)
            text = font.render(str(count), True, THECOLORS['black'])
            dis.blit(text, (x + 10, 50))
        count+=1
    pygame.display.update()

quit()