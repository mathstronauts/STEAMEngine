# SEV Beginner - Week 2 Alien and Collision Detection
# Students will learn to add their alien sprite and detect collisions

import pgzrun
import random

WIDTH = 800
HEIGHT = 600

background_img = "mars_background"

# initialize characters - Actor("image_file", (x_position, y_position) )
player = Actor("spaceship_beg_up")
player.midbottom=(WIDTH//2, HEIGHT)

alien = Actor("alien_beg_sprite")
alien.pos = (random.randint(40, WIDTH-40), random.randint(100, HEIGHT-40))  # pos same as center

def update():
    # check for keyboard input
    # test with spacebar
    # if (keyboard.space):
        # player.x += 5
        # player.image = "alien_beg_sprite"
    if (keyboard.up == 1) and (player.top > 0):
        player.y += -5  # moving up, so moving in negative y direction
    elif (keyboard.down == 1) and (player.bottom < HEIGHT):
        player.y += 5  # moving down, so moving in positive y direction
    elif (keyboard.left == 1) and (player.left > 0):
        player.x += -5  # moving left, so negative x direction
    elif (keyboard.right == 1) and (player.right < WIDTH):
        player.x += 5  # moving right, so positive x direction

    # if player collides with the alien
    if (player.colliderect(alien) == 1):  # colliderect() tests if two rectangles overlap, return 1 when there is a collision, 0 when no collision
        alien.pos = (random.randint(40, WIDTH-40), random.randint(100, HEIGHT-40)) # make the alien appear at a new random position

def draw():
    screen.clear()
    screen.blit(background_img, (0, 0))
    player.draw()
    alien.draw()
    
pgzrun.go()
