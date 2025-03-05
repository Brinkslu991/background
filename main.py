# Pygame game template

import pygame
import sys
import config # Import the config module

# Draw boat
def draw_ball(screen):
    pygame.draw.ellipse(screen, config.BROWN, (200,300, 300,150))
    pygame.draw.ellipse(screen, config.TAN, (270, 320, 10, 100))
    pygame.draw.ellipse(screen, config.TAN, (310, 320, 10, 100))
    pygame.draw.ellipse(screen, config.TAN, (350, 320, 10, 100))
    pygame.draw.ellipse(screen, config.TAN, (390, 320, 10, 100))
    pygame.draw.ellipse(screen, config.TAN, (430, 320, 10, 100))

text_font = pygame.font.SysFont('Comic Sans MS', 30)

def init_game ():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events ():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x,y))

    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here
    running = True
    while running:
        running = handle_events()
        screen.fill(config.BLUEGAMBIT) # Use color from config

        draw_text('Bread', text_font, (0,0,0), 220, 150)

        draw_ball(screen)

        pygame.display.flip()
        
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # Use the clock to control the frame rate

        

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()
