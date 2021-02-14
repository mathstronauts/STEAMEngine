# SEV Advanced - Week 1 Intro to Pygame Zero
# Students will learn to Students will learn to:
# create a game window, fill screen with colour, display a background image, create a player sprite, and read user input

import pgzrun
import random

# define some colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

WIDTH = ____ # set width of the screen
HEIGHT = ___ # set height of the screen

BACKGROUND_IMG =  # enter image file name of game background

# initialize characters - Actor("image_file", (x_position, y_position) )
player = Actor("player_ship", midright = (WIDTH - 15, HEIGHT//2))

# DRAW SCREEN FUNCTION        
def draw():
    screen.clear() # clear the screen
    screen.blit(BACKGROUND_IMG, (0,0))
    # draw player

# UPDATE SCREEN FUNCTION
def update():
    # call player update function

def updatePlayer():
    # check for user input
    if ():
        # moving up (negative y direction)
    elif ():
        # moving down (postive y direction)

    # prevent player from moving off screen
    if ():
        # set player position
    if ():
        # set player position
    
pgzrun.go() # we need this function to run Pygame Zero from the IDLE window
