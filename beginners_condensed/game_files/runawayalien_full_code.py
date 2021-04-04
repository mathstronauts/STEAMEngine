# SEV Beginner - Condensed Full Code

import pgzrun
import random

WIDTH = 800
HEIGHT = 600

background_img = "mars_background"
score = 0 # initialize score variable

# initialize characters - Actor("image_file", (x_position, y_position) )
player = Actor("spaceship_beg_up")
player.midbottom=(WIDTH//2, HEIGHT)

alien = Actor("alien_beg_sprite")
alien.pos = (random.randint(40, WIDTH-40), random.randint(100, HEIGHT-40))  # pos same as center

# background music
sounds.music_upbeat.play(-1)

def update():
    global score # since we are changing the variable score within a function, we need to add the keyword global
    if (keyboard.up == 1) and player.top > 0:
        player.y += -5  
        player.image = "spaceship_beg_up"
    elif (keyboard.down == 1) and player.bottom < HEIGHT:
        player.y += 5  
        player.image = "spaceship_beg_down"
    elif (keyboard.left == 1) and player.left > 0:
        player.x += -5  
        player.image = "spaceship_beg_left"
    elif (keyboard.right == 1) and player.right < WIDTH:
        player.x += 5  
        player.image = "spaceship_beg_right"

    # if player collides with the alien
    if player.colliderect(alien) == 1:  # colliderect() tests if two rectangles overlap, return 1 when there is a collision, 0 when no collision
        alien.pos = (random.randint(40, WIDTH-40), random.randint(100, HEIGHT-40)) # make the alien appear at a new random position
        sounds.alien_device.play()
        score += 1  #  score = score + 1

def draw():
    screen.clear()
    screen.blit(background_img, (0, 0))
    player.draw()
    alien.draw()

    # draw some text on the screen
    show_score = str(score)
    screen.draw.text(show_score, fontsize=40, topright=(750,21), color='white') # students may need to adjust coordinates depending on where there box is on their background
    
pgzrun.go()
