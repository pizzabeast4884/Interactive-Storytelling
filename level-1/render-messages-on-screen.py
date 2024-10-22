import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Interactive Story")

# Set up fonts
font = pygame.font.Font(None, 36)

# Colors
WHITE = (200, 255, 210)
BLACK = (50, 50, 50)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(WHITE)

    # Render some text
    text = font.render("hello welcome to the game please enter your name ", True, BLACK)
    screen.blit(text, (50, 50))

    # Update the display
    pygame.display.flip()

pygame.quit()