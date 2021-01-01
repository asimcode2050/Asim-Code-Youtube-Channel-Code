import pygame
pygame.init()
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

width = 400
height = 600
our_screen  = pygame.display.set_mode((width,height))
our_screen.fill(black)

while True:
    pygame.draw.circle(our_screen,green,(250,300), 20)
    pygame.display.update()


