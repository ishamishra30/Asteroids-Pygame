import pygame, sys, os, random, math
from pygame.locals import *

pygame.init()                      
fps = pygame.time.Clock()

#colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

#globals
WIDTH = 800
HEIGHT = 600      
time = 0

#canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Asteroids')
        
#load images
bg = pygame.image.load(os.path.join('images','bg.jpg'))
debris = pygame.image.load(os.path.join('images','debris2_brown.png'))
ship = pygame.image.load(os.path.join('images','ship.png'))

ship_x = WIDTH/2 - 50
ship_y = HEIGHT/2 - 50
ship_angle = 0

def rot_center(image, angle):
    """rotate a Surface, maintaining position."""

    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

# draw game function
def draw(canvas):
    global time
    canvas.fill(BLACK)
    canvas.blit(bg,(0,0))
    canvas.blit(debris,(time*.3,0))
    canvas.blit(debris,(time*.3-WIDTH,0))
    time = time + 1


    canvas.blit( rot_center(ship,ship_angle) , (ship_x, ship_y))


# handle input function
def handle_input():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()   

# update the screen
def update_screen():
    pygame.display.update()
    fps.tick(60)

# asteroids game loop
while True:
    draw(window)
    handle_input()
    # game_logic()
    update_screen()
