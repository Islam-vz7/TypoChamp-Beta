import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Credits Screen")

# Set up fonts
font = pygame.font.Font(None, 36)

# Define credits text
credits_text = [
    "Credits",
    "",
    "Developer: Your Name",
    "Artwork: Artist Name",
    "Music: Composer Name",
    "",
    "Thank you for playing!",
    "",
    "Press ESC to return to the main menu",
]

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Display credits text
    y_offset = 50
    for line in credits_text:
        text_surface = font.render(line, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(screen_width // 2, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += 40

    # Update the display
    pygame.display.flip()

# Note: This is a basic example, and you can customize it further based on your needs,
# such as adding images, animations, or additional information in the credits.
