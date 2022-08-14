from cmath import rect
from curses.ascii import ESC
from random import randint
from turtle import width
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("First Python Game")
clock = pygame.time.Clock()
test_font = pygame.font.Font('./font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('./graphics/Sky.png').convert_alpha()
ground_surf = pygame.image.load('./graphics/ground.png').convert_alpha()
score_surf = test_font.render('Hello World!', True, pygame.color.Color('#2a0878'))
score_rect = score_surf.get_rect(center = (400, 50))

snail_surf = pygame.image.load("./graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (810, 300))
snail_speed = randint(2, 5)

player_surf = pygame.image.load("./graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom = (50,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surf, (0,0))
    screen.blit(ground_surf, (0,300))
    pygame.draw.rect(screen, pygame.color.Color('#09bced'), score_rect)
    pygame.draw.rect(screen, pygame.color.Color('#09bced'), score_rect, 14)
    screen.blit(score_surf, score_rect)
    snail_rect.x -= snail_speed
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    # Reset postion and assign random speed
    if snail_rect.x < -50:
       snail_rect.x = 810
       snail_speed = randint(2, 5)

    pygame.display.update()
    clock.tick(60)