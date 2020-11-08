# SEV Beginner - Week 1 Intro to Pygame Zero TEMPLATE
# Students will learn to create a game window, fill screen with colour, display a background image, create a junk sprite, and move the junk sprite

import pgzrun
import random

# define some colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

WIDTH = ____  # enter the width of the screen
HEIGHT = ___  # enter the height of the screen

BACKGROUND_IMG = "_________"  # enter image file name of game background

# initialize characters - Actor("image_file", (x_position, y_position) )
player = Actor()

# DRAW SCREEN FUNCTION
def draw():
    # clear screen
    screen.blit(BACKGROUND_IMG, (0, 0))
    # draw player

# UPDATE SCREEN FUNCTION
def update():
    if ():
        # player moves up
    elif ():
        # player moves down
    elif ():
        # player moves left
    elif ():
        # player moves right


pgzrun.go() # we need this function to run Pygame Zero from the IDLE window
