import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Interactive Story with Character Movement")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the character
player_size = 50
player_pos = [400, 300]
player_speed = 5

# Main loop
running = True
while running:
    # Check for events (e.g., if the user closes the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the list of keys currently being pressed
    keys = pygame.key.get_pressed()

    # TASK: Use the arrow keys to move the character around the screen
    # Hint: Adjust the player_pos list using player_speed
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

    # Update the display
    pygame.display.flip()

pygame.quit()

# EXTENSION: Try changing the player's color or size. Can you add a second character to move?