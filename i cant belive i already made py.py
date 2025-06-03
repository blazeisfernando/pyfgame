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
clock = pygame.time.Clock()
FPS = 60

#gamelooppt1
run = True
#gamewindow
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#x,y,Widtht,heitgt
#THE HIGHER THE LOWER!!!!!!!!
player = pygame.Rect((250, 250, 50, 50))
ground = pygame.Rect((150, 300, 300, 50))
ground_copy = ground.copy()
ground_copy.x += 350
#jumpy stuff
velocity_y = 0         # How fast the player is falling
gravity = 0.2          # Gravity strength
jump_strength = -8
is_jumping = False     # True when in the air


#gamelooppt2

#run = True
while run == True:
    clock.tick(FPS)
    

    #screen.fill((135, 206, 235))
    #pygame.draw.rect(screen,(0, 128, 0), ground)
    #pygame.draw.rect(screen,(255, 0, 0), player)
    key = pygame.key.get_pressed()

    #velocity_y += gravity
    #player.y += velocity_y

    #if player.colliderect(ground):
        #player.bottom = ground.top  # Snap to ground
        #velocity_y = 0
        #is_jumping = False



    if key[pygame.K_a] == True:
        player.move_ip(-10, 0)
    elif key[pygame.K_d] == True:
        player.move_ip(10, 0)
    elif key[pygame.K_w] == True:
        player.move_ip(0, -1)
    #elif key[pygame.K_SPACE] == True:
        #player.move_ip(0, -2)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 10)

    if key[pygame.K_SPACE] and not is_jumping:
        
        velocity_y = jump_strength
        is_jumping = True

    velocity_y += gravity
    player.y += velocity_y

    

    if player.colliderect(ground):
        player.bottom = ground.top  # Snap to ground
        velocity_y = 0
        is_jumping = False
    else:
        is_jumping = True


    screen.fill((135, 206, 235))
    pygame.draw.rect(screen,(0, 128, 0), ground)
    pygame.draw.rect(screen,(255, 0, 0), player)
    pygame.draw.rect(screen, (0, 200, 0), ground_copy)

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False



        


    pygame.display.update()


pygame.quit()




#pygame.display.set_mode()    