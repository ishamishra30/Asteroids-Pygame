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

# draw game function
def draw(canvas):
    global time
    canvas.fill(BLACK)
    canvas.blit(bg,(0,0))
    canvas.blit(debris,(time*.3,0))
    canvas.blit(debris,(time*.3-WIDTH,0))
    time = time + 1
    canvas.blit(ship, (WIDTH/2 -50,HEIGHT/2 -50))

# (0,0)
# (width,0)
# (0,height)
# (width,height)

# handle input function
def handle_input():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()   

def update_screen():
    pygame.display.update()
    fps.tick(60)

# asteroids game loop
while True:
    draw(window)
    handle_input()
    # game_logic()
    update_screen()
