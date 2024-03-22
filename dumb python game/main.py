import pygame
from sys import exit

# starts pygame
pygame.init()
# starts the screen
screen = pygame.display.set_mode((800, 400))
# sets the game title
pygame.display.set_caption("Placeholder Title")
# sets the framerate
clock = pygame.time.Clock()
# creates a font
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

# creates a surface/image to put on screen, on this case the sky. the .convert just converts the png file into something pygame
#  the png file into something pygame can utilize more easily.
sky_surface = pygame.image.load('graphics/Sky.png').convert()
# same thing, but with the ground
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game', False, 'black')

# calling the enemy, convert_alpha respects the alpha values, so it doesn't do any weird shit.
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
# moves the snail x position to a variable
snail_x_pos = 600
# creating the hooman
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
# creates the rectangle for the player, really easier.
player_rect = player_surf.get_rect(midbottom = (80, 300))

# creates the loop for the game
while True:
    # creates the for loop that searches for the X press and if it is pressed it closes the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # blit essentially means block image transfer, which is a fancy way of saying put image on top of image.
    screen.blit(sky_surface,(0,0))
    # pygame always draws in order of when we run the code, so calling the ground after the sky is necessary.
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(325,50))
    # moves the snail x position by one by updating its variable
    snail_x_pos -= 4 
    # makes an if statement that makes the snail go back to the end of the screen    
    if snail_x_pos < -100:
        snail_x_pos = 800
    # puts the snail on screen, using variables as position
    screen.blit(snail_surface,(snail_x_pos,265))
    # makes the player go boom
    player_rect.left += 1
    # puts the player on screen.
    screen.blit(player_surf,player_rect)
   
    # this will update every frame
    pygame.display.update()
    # sets le frame rate
    clock.tick(60)