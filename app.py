from random import randint
import pygame
from sys import exit

def display_score():
    currentTime = pygame.time.get_ticks() / 1000 - startTime
    score_surf = game_font.render(f'Score: {currentTime:.0f}', True, '#2a0878')
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return currentTime

def obstacle_movement(obstacle_list, speed):
    if obstacle_list:
        for i,obstacle_rect in enumerate(obstacle_list):
            if obstacle_rect.right < 0:
                obstacle_list.pop(i)

            obstacle_rect.x -= speed
            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else:
                screen.blit(fly_surf, obstacle_rect)

        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return True
    return False


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("First Python Game")
clock = pygame.time.Clock()
game_font = pygame.font.Font('./font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('./graphics/Sky.png').convert_alpha()
ground_surf = pygame.image.load('./graphics/ground.png').convert_alpha()

# Obstacle
snail_surf = pygame.image.load("./graphics/snail/snail1.png").convert_alpha()
snail_speed = randint(6, 10)

obstacle_rect_list  = []

fly_surf = pygame.image.load("./graphics/Fly/Fly1.png").convert_alpha()

player_surf = pygame.image.load(
    "./graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(50, 300))
player_gravity = 0

# intro screen
player_stand = pygame.image.load("./graphics/Player/player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_title = game_font.render('Jumping Maniac', True, '#8FED86')
game_title_rect = game_title.get_rect(center = (400, 75))

game_message = game_font.render('Press SPACE to start', True, '#00D8AE')
game_message_rect = game_message.get_rect(center = (400, 350))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

isGameOver = True
startTime = 0
score = 0

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
            if event.type == obstacle_timer:
                if randint(0,1):
                    obstacle_rect_list.append(snail_surf.get_rect(bottomright = (randint(900,1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900,1100), 210)))

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                isGameOver = False
                startTime = pygame.time.get_ticks() / 1000


    if not isGameOver:
        screen.blit(sky_surf, (0,0))
        screen.blit(ground_surf, (0,300))
        score = display_score()

        ### Obstacle movement
        speed = randint(6, 20)
        obstacle_rect_list = obstacle_movement(obstacle_rect_list, speed)

        ### player
        player_gravity += 1
        player_rect.y += player_gravity

        if player_rect.bottom >= 300:
            player_rect.bottom = 300

        screen.blit(player_surf, player_rect)

        ## Collision
        isGameOver = collisions(player_rect, obstacle_rect_list)
    else:
        obstacle_rect_list.clear()
        score_message = game_font.render(f'Your score: {score:.0f}', True, '#F9F871')
        score_message_rect = score_message.get_rect(center=(400, 350))

        screen.fill('#1a75c9')
        screen.blit(game_title, game_title_rect)
        screen.blit(player_stand, player_stand_rect)
        if score > 0:
            screen.blit(score_message, score_message_rect)
        else:
            screen.blit(game_message, game_message_rect)

    pygame.display.update()
    clock.tick(60)