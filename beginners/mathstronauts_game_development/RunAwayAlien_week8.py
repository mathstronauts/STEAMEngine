# SEV Beginner - Week 1 Intro to Pygame Zero
# Students will learn to create a game window, fill screen with colour, display a background image, create a junk sprite, and move the junk sprite

import pgzrun

# define some colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

WIDTH = 800
HEIGHT = 600

background_img = "mars_background"

# initialize characters - Actor("image_file", (x_position, y_position) )
player = Actor("spaceship_beg_up", midbottom = (400, 600))

def update():
    if (keyboard.up == 1) and (player.top > 0):
        player.y += -5  
    elif (keyboard.down == 1) and (player.bottom < HEIGHT):
        player.y += 5  
    elif (keyboard.left == 1) and (player.left > 0):
        player.x += -5  
    elif (keyboard.right == 1) and (player.right < WIDTH):
        player.x += 5

def draw():
    screen.clear()  # clear the screen
    screen.blit(background_img, (0, 0))  # draw background image
    player.draw()
    

pgzrun.go()
