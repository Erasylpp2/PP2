import pygame
import random

# Initialize pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Player
player_img = pygame.image.load('player.png')
player_rect = player_img.get_rect(center=(WIDTH // 2, HEIGHT - 100))
player_speed = 5

# Coins
coins = []
coin_img = pygame.image.load('coin.png')

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed
    
    # Draw player
    screen.blit(player_img, player_rect)
    
    # Generate coins
    if random.randint(0, 100) < 3:
        coin_rect = coin_img.get_rect(center=(random.randint(50, WIDTH-50), 0))
        coins.append(coin_rect)
    
    # Draw coins
    for coin_rect in coins:
        screen.blit(coin_img, coin_rect)
    
    # Collision detection with coins
    collected_coins = [coin for coin in coins if player_rect.colliderect(coin)]
    for coin in collected_coins:
        coins.remove(coin)
        # Increment score
        
    # Show number of collected coins
    font = pygame.font.Font(None, 36)
    text = font.render("Coins: " + str(len(collected_coins)), True, GREEN)
    screen.blit(text, (WIDTH - 150, 20))
    
    pygame.display.flip()

pygame.quit()
