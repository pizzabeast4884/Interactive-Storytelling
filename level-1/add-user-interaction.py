import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Interactive Story")

# Set up fonts
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLUE = (40, 137, 247)
BLACK = (0, 0, 0)
GREEN = (200, 255, 200)

# Method used to print new lines
def render_text(lines):
    y_offset = 0
    for line in lines:
        text_surface = font.render(line, True, (0, 0, 0))
        screen.blit(text_surface, (50, 50 + y_offset))
        y_offset += font.get_linesize()

# Story state
scene = 1
hungry = True
wallet = 500

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
            elif event.key == pygame.K_3:
                hungry = False
                scene = 3
            elif event.key == pygame.K_c:
                scene = 99
            elif event.key == pygame.K_b:
                scene = 10000
                   

    # Fill the screen with white
    screen.fill(WHITE)

    # Render text based on the scene
    if scene == 1:
        screen.fill(BLUE)
        text = "hello welcome to the game!"
        lines = text.split('\n')
    elif scene == 2:
        screen.fill(GREEN)
        lines = [
            "welcome to the shop choose and item.",
            "gun $50",
            "food $20",
            "water$30",
            "horse$100",
            "",
            "",
            "",
            "",
            "click 3 to continue to the oregan trail",
            "to begin the game"
        ]
    elif scene == 3:
        text = font.render("you got a pizza well done!", True, BLACK)
    elif scene == 4:
        text = font.render("you know better than this!", True, BLACK)
    elif scene == 99:
        lines = [
            "controls.",
            "B: wallet ",
            "i: inventory",
            "c: controls"
        ]
    elif scene == 10000:
        lines = [
            str(wallet)



        ]
    render_text(lines)

    # Update the display
    pygame.display.flip()

pygame.quit()