import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

# Load images
player_img = pygame.image.load("car.png")
coin_img = pygame.image.load("coin.png")

player_x = WIDTH // 2
player_y = HEIGHT - 100
player_speed = 5

coin_x = random.randint(50, WIDTH - 50)
coin_y = -50
coin_speed = 5

score = 0
font = pygame.font.SysFont(None, 36)

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Keep player in screen
    player_x = max(0, min(WIDTH - player_img.get_width(), player_x))

    # Move coin
    coin_y += coin_speed
    if coin_y > HEIGHT:
        coin_y = -50
        coin_x = random.randint(50, WIDTH - 50)

    # Collision
    player_rect = player_img.get_rect(topleft=(player_x, player_y))
    coin_rect = coin_img.get_rect(topleft=(coin_x, coin_y))

    if player_rect.colliderect(coin_rect):
        score += 1
        coin_y = -50
        coin_x = random.randint(50, WIDTH - 50)

    # Draw
    screen.blit(player_img, (player_x, player_y))
    screen.blit(coin_img, (coin_x, coin_y))

    score_text = font.render(f"Coins: {score}", True, (255, 255, 255))
    screen.blit(score_text, (WIDTH - 150, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
