import enum
from random import randint
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("First Python Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font('./font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('./graphics/Sky.png').convert_alpha()
ground_surf = pygame.image.load('./graphics/ground.png').convert_alpha()

# score_surf = test_font.render('Hello World!', True, '#2a0878')
# score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load("./graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(810, 300))
snail_speed = randint(6, 10)

player_surf = pygame.image.load(
    "./graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(50, 300))

restartBtn_surf = test_font.render("Restart", True, '#2a0878')
restartBrn_rect = restartBtn_surf.get_rect(center=(400, 200))

player_gravity = 0

isGameOver = False

while True:
    for i, event in enumerate(pygame.event.get()):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not isGameOver:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                    player_gravity -= 22 + player_gravity
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom == 300:
                    player_gravity -= 22 + player_gravity
        else:
            if event.type == pygame.MOUSEBUTTONDOWN and restartBrn_rect.collidepoint(event.pos) and event.button == 1:
                isGameOver = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                isGameOver = False


    if not isGameOver:
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0,300))
        pygame.draw.rect(screen, '#09bced', score_rect)
        pygame.draw.rect(screen, '#09bced', score_rect, 14)
        screen.blit(score_surf, score_rect)

        # snail
        snail_rect.x -= snail_speed
        # Reset postion and assign random speed
        if snail_rect.x < -50:
            snail_rect.x = 810
            snail_speed = randint(6, 20)

        if snail_rect.colliderect(player_rect):
            isGameOver = True
            snail_rect.x = 810

        screen.blit(snail_surf, snail_rect)

        # player
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player_surf, player_rect)
    else:
        screen.fill('Yellow')
        pygame.draw.rect(screen, '#09bced', restartBrn_rect)
        pygame.draw.rect(screen, '#09bced', restartBrn_rect, 14)
        screen.blit(restartBtn_surf, restartBrn_rect)

    pygame.display.update()
    clock.tick(60)