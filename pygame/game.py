from sys import exit

import pygame


pygame.init() 
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Mein Python Spiel')
clock = pygame.time.Clock()

# test_surface = pygame.Surface((100, 200))
# test_surface.fill('red')

test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
text_surface = test_font.render('My game', False, 'Black')

sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()  # remove alpha values
snail_x_pos = 600

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
# -> kombiniert durch sprite (kommt noch)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    snail_x_pos -= 4
    if snail_x_pos < -50:
        snail_x_pos = 820
    screen.blit(snail_surf, (snail_x_pos, 260))
    screen.blit(player_surf, player_rect)  # place surface in position of rectangle

    pygame.display.update()
    clock.tick(60)



