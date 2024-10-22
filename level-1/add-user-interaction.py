import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Interactive Story")

# Set up fonts
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (200, 255, 200)

# Story state
scene = 1

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                
                scene = 1
            elif event.key == pygame.K_2:
                scene = 2
            elif event.key == pygame.K_3 :
                
                if scene == 1:
                    scene = 4
                else: 
                    scene = 3
                   

    # Fill the screen with white
    screen.fill(WHITE)

    # Render text based on the scene
    if scene == 1:
        text = font.render("You are in a dark forest. Press 2 to go to the castle.", True, BLACK)
    elif scene == 2:
        screen.fill(GREEN)
        text = font.render("You are now in the castle. Press 3 to go get a pizza.", True, BLACK)
    elif scene == 3:
        text = font.render("you got a pizza well done!", True, BLACK)
    elif scene == 4:
        text = font.render("you know better than this!", True, BLACK)

    screen.blit(text, (50, 50))

    # Update the display
    pygame.display.flip()

pygame.quit()