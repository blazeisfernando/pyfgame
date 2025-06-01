#wow look at this
import pygame
import os

pygame.init()
script_dir = os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(script_dir, "assets", "New Project.png")

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
pygame.display.set_caption("Wow! Look at This 🎮")
icon = pygame.image.load(icon_path)
pygame.display.set_icon(icon)


#gamelooppt1
run = True
#gamewindow
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#x,y,Widtht,heitgt
#THE HIGHER THE LOWER!!!!!!!!
player = pygame.Rect((250, 250, 50, 50))
ground = pygame.Rect((150, 300, 300, 50))


#gamelooppt2

run = True
while run == True:



    screen.fill((135, 206, 235))
    pygame.draw.rect(screen,(0, 128, 0), ground)
    pygame.draw.rect(screen,(255, 0, 0), player)
    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()


pygame.quit()

#pygame.display.set_mode()