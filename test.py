import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Enter Your Name")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font(None, 36)

# Input box variables
input_box = pygame.Rect(290, 200, 200, 32)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
text = ''
text_surface = font.render(text, True, color)
active = False

# Game variables
game_running = False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive
        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    print(text)  # You can store or display the entered name as needed
                    text = ''
                    game_running = True  # Start the game
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                else:
                    text += event.unicode
                text_surface = font.render(text, True, color)

    # Draw background
    screen.fill(white)

    # Draw input box and text
    pygame.draw.rect(screen, color, input_box, 2)
    screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))

    # Update display
    pygame.display.flip()

    # Start the game loop if the name is entered
    if game_running:
        # Your game code goes here
        # For example, a simple game loop that quits when the user presses the close button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False

        # Draw game elements and update display
        screen.fill(black)
        # Your game drawing and logic code goes here

        pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
