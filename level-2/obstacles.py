import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Interactive Story with Character Movement")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the character
player_size = 50
player_pos = [400, 300]
player_speed = 5

# Set up an object to interact with
object_pos = [200, 150]
object_size = 50

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the list of keys currently being pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the player character
    pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1], player_size, player_size))

    # Draw the object
    pygame.draw.rect(screen, GREEN, (object_pos[0], object_pos[1], object_size, object_size))

    # Check for collision between player and object
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    object_rect = pygame.Rect(object_pos[0], object_pos[1], object_size, object_size)

    if player_rect.colliderect(object_rect):
        # Display a message if the player reaches the object
        font = pygame.font.Font(None, 36)
        text = font.render("You found the object!", True, BLACK)
        screen.blit(text, (250, 50))

    # Update the display
    pygame.display.flip()

pygame.quit()

# EXTENSION: Add more objects. Can you create a condition that ends the game when all objects are collected?