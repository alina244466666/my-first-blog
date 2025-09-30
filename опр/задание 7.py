import pygame
from pygame.color import THECOLORS

pygame.init()
dis = pygame.display.set_mode((700,500))
dis.fill(THECOLORS['gray'])

font = pygame.font.SysFont('couriernew', 30)
text = font.render(('snowman'), True, THECOLORS['black'])
dis.blit(text, (2, 1))
r = pygame.Rect(100,100,100,100)




dis_over = False
while not dis_over:
    '''dt = clock.tick(60)
    timer += dt'''
    for event in pygame.event.get():
        pygame.draw.circle(dis, (255, 225, 255), (65, 70), 15)
        pygame.draw.circle(dis, (255, 225, 255), (65, 108), 25)
        pygame.draw.circle(dis, (255, 225, 255), (65, 158), 35)
        pygame.draw.circle(dis, (0, 0, 100), (65, 110), 3)
        pygame.draw.circle(dis, (0, 0, 100), (65, 155), 3)
        pygame.draw.circle(dis, (0, 0, 100), (60, 70), 2)
        pygame.draw.circle(dis, (0, 0, 100), (70, 70), 2)
        pygame.draw.rect(dis, (120, 130, 105), (120, 70, 5, 120))
        pygame.draw.lines(dis, (120, 110, 105), False, [(90, 100), (120, 130)])
        pygame.draw.lines(dis, (120, 110, 105), False, [(37, 100), (30, 150)])
        pygame.draw.polygon(dis, (120, 150, 150), [(70, 30), (85, 60), (45, 60), (55, 30)])
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()

quit()
