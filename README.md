.import pygame
import random

# Initialize pygame
pygame.init()  n

# Screen
screen = pygame.display.set_mode((800, 600))'
pygame.display.set_caption("Simple Gun Game")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Player
player_x = 370
player_y = 500
player_speed = 5

# Bullet
bullet_x = 0
bullet_y = 500
bullet_speed = 10
bullet_state = "ready"

# Enemy
enemy_x = random.randint(0, 750)
enemy_y = 50
enemy_speed = 3

# Score
score = 0
font = pygame.font.Font(None, 36)

def show_score():
    text = font.render("Score: " + str(score), True, white)
    screen.blit(text, (10, 10))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    pygame.draw.rect(screen, red, (x + 16, y, 5, 10))

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Key controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_SPACE]:
        if bullet_state == "ready":
            bullet_x = player_x
            fire_bullet(bullet_x, bullet_y)

    # Bullet movement
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_speed

    if bullet_y <= 0:
        bullet_y = 500
        bullet_state = "ready"

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y > 600:
        enemy_y = 50
        enemy_x = random.randint(0, 750)

    # Collision
    if abs(enemy_x - bullet_x) < 30 and abs(enemy_y - bullet_y) < 30:
        bullet_y = 500
        bullet_state = "ready"
        enemy_x = random.randint(0, 750)
        enemy_y = 50
        score += 1

    # Draw player
    pygame.draw.rect(screen, white, (player_x, player_y, 50, 50))

    # Draw enemy
    pygame.draw.rect(screen, red, (enemy_x, enemy_y, 50, 50))

    show_score()

    pygame.display.update()

pygame.quit()
