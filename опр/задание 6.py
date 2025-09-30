'''
with open("hello.txt", "w+") as file:
    file.write("Hello world\nHello work\n")
    file.seek(0)
    content = file.read()
    print(content)

with open("hello.txt", "w+") as file:
    file.write("Hello world\n")
    file.seek(8)
    content = file.read()
    print(content)'''
'''from gettext import install'''

'''pip install(pygame)'''

import pygame

pygame.init()
dis = pygame.display.set_mode((500,400))
r = pygame.Rect(100,100,100,100)

dis_over = False
while not dis_over:
    for event in pygame.event.get():
        #pygame.draw.lines(dis,(120, 50, 50), False, [(40, 80), (100, 10)])
        pygame.draw.lines(dis, (120, 50, 50), False, [(80, 10), (101, 100)])
        pygame.draw.lines(dis, (120, 50, 50), False, [(80, 10), (50, 10)])
        pygame.draw.polygon(dis, (120, 50, 50), [(100, 100), (0, 100), (50, 10)])
        pygame.draw.circle(dis, (180, 160, 50), (50, 70), 15)
        pygame.draw.rect(dis, (180, 160, 50), (5, 90, 90, 90))
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()

quit()



