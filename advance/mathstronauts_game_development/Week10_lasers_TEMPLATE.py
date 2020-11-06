# SEV Advanced - Week 10 Adding Shooting Features TEMPLATE
# Students will learn to use lists to fire and keep track of lasers

# COPY AND PASTE YOUR CODE HERE:




# ________________________CREATE UPDATELASERS FUNCTION__________________________
def updateLasers():
    global lasers, score 
    x_speed = __ # add laser speed
    for i in range(len(lasers)):
        lasers[i].x += x_speed
        if lasers[i].right < __:  # if laser moves off the screen, remove if from our game list
            lasers[i].status = 1

        # check for collisions with lasers (just debris and satellites)
        # if debris collide with lasers
            # mark laser for removal
            # reinitialize debris
            # change score
        # elif satellite collide with lasers
            # mark laser for removal
            # reinitialize satellite
            # change score

    lasers = mathstropy.pgzero.listCleanup(lasers)  # this helps make sure our lists are working properly

# activating lasers (template code - DO NOT DELETE)
player.laserActive = 1

def makeLaserActive():
    global player
    player.laserActive = 1

def fireLasers(sprite):
    if player.laserActive == 1:  # active status is used to prevent continuous shoot when holding space key
        player.laserActive = 0
        clock.schedule(makeLaserActive, 0.2)  # schedule an event (function, time afterwhich event will occur)
        sounds.laserfire02.play()
        lasers.append(sprite)
        lasers[len(lasers) - 1].status = 0
    
pgzrun.go()
