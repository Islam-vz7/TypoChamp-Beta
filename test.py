import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Word Fall Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the font
font = pygame.font.Font(None, 36)

# Load a list of words
word_list = ["python", "game", "pygame", "coding", "keyboard", "challenge", "fun"]

# Initialize variables
falling_words = []
input_word = ""
score = 0

# Function to generate a new falling word
def generate_falling_word():
    return {
        "word": random.choice(word_list),
        "x": random.randint(0, width - 100),
        "y": 0
    }

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                input_word = input_word[:-1]
            elif event.key == pygame.K_RETURN:
                for word in falling_words:
                    if input_word == word["word"]:
                        falling_words.remove(word)
                        score += 1
                input_word = ""
            elif event.key in range(97, 123):  # Check if the key is a lowercase letter
                input_word += event.unicode

    # Update falling words
    for word in falling_words:
        word["y"] += 5

    # Generate a new falling word
    if random.randint(0, 100) < 5:
        falling_words.append(generate_falling_word())

    # Check for collision with the bottom
    for word in falling_words:
        if word["y"] > height - 50:
            falling_words.remove(word)

    # Draw everything
    screen.fill(white)

    for word in falling_words:
        word_surface = font.render(word["word"], True, black)
        screen.blit(word_surface, (word["x"], word["y"]))

    input_surface = font.render(input_word, True, black)
    screen.blit(input_surface, (width // 2 - 50, height - 50))

    # Display the score
    score_surface = font.render(f"Score: {score}", True, black)
    screen.blit(score_surface, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)
