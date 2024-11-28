import pygame

pygame.init()

# Set up the display
screen_width, screen_height = 1080, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Interactive Story")

# Set up fonts
font = pygame.font.Font(None, 36)


file_name ="oregan.jpg"

def prepare_backround(file_name):
    backround_image = pygame.image.load(file_name)
    backround_image = pygame.transform.scale(backround_image, (screen_width, screen_height))
    screen.blit(backround_image, (0, 0))

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
inventory = []

# Main loop
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:  
                scene = 1
                file_name = "oregan.jpg"
            elif event.key == pygame.K_2: 
                scene = 2 
                file_name = "image.jpg"
            elif event.key == pygame.K_3:
                scene = 3
                file_name = "image2.jpg"
            elif event.key == pygame.K_LEFT:
                print("pressed left")
                scene = 4 
                file_name = "image3.jpg"
                file_name = ""
            elif event.key == pygame.K_i:
                scene = 100000
            elif event.key == pygame.K_c:
                scene = 99
            elif event.key == pygame.K_b:
                scene = 10000
            elif event.key == pygame.K_g:
                inventory.append("gun")
            elif event.key == pygame.K_f:
                inventory.append("food")

    prepare_backround(file_name)

                   

  
    # Render text based on the scene
    if scene == 1:
       
        text = "welcome to the oregan trail"
        lines = text.split('\n')
    elif scene == 2:
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
            "",
            "",
            "click 3 to continue to the oregan trail",
            "to begin the game"
        ]
    elif scene == 3:
        lines = [
            "you left Boston.",
            "",
            "",
            "",
            "",
            "",
            ""
            "",
            "you have come across a split in the road",
            "choose left or right",
            ]
    elif scene == 4:
        lines = [
            " you lost 50 hunger points points",
            "after climbing a mountain",
            "",
            "",
            "",
            "",
            "press e to regenerate your",
            "hunger points",
            "press forward to continue onwards"
            ]


    elif scene == 100000:
       lines = ["inventory"]
       lines = lines + inventory
    elif scene == 99:
        lines = [
            "controls.",
            "B: wallet ",
            "i: inventory",
            "c: controls",
            "e: regen hunger"
        ]
    elif scene == 10000:
        lines = [
            str(wallet)



        ]
    render_text(lines)

    # Update the display
    pygame.display.flip()

pygame.quit()