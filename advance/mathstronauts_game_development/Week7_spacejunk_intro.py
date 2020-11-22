# SEV Advanced - Week 1 Intro to Pygame Zero
# Students will learn to Students will learn to:
# create a game window, fill screen with colour, display a background image, create a player sprite, and read user input

import pgzrun

WIDTH = 1000
HEIGHT = 600

BACKGROUND_IMG = "space_game_background"

player = Actor("player_ship", midright = (WIDTH - 15, HEIGHT//2))

# game loop
def update():
    # check for user input
    if keyboard.up == 1:
        player.y += -5  # moving up is in negative y direction
    elif keyboard.down == 1:
        player.y += 5  # moving down is in the postive y direction

    # prevent player from moving off screen
    if player.top < 0:
        player.top = 0
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT

def draw():
    screen.clear()
    screen.blit(BACKGROUND_IMG, (0,0))
    player.draw()
    
        
pgzrun.go()
