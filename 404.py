import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Falling Words")

# Define colors
white = (255, 255, 255)

# Create a Clock object to control the frame rate
clock = pygame.time.Clock()

# Define the Word class
class Word(pygame.sprite.Sprite):
    def __init__(self, text, x, y):
        super().__init__()
        self.image = font.render(text, True, white)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def update(self):
        self.rect.y += 2  # Adjust the falling speed


# Set up the font
font = pygame.font.Font(None, 36)

# Create a sprite group for the words
all_words = pygame.sprite.Group()

def read_words():
         level1_words = []
         with open("words.txt", "+r") as file:
            for line in file:
              word = line.strip()
              if 1 <= len(word) <= 5:
                level1_words.append(word)
         return level1_words
      
# Function to add a new falling word
def add_word():
    word_list = read_words()  # Add more words as needed
    word_text = random.choice(word_list)
    x = random.randint(0, width - 100)
    y = 0
    word = Word(word_text, x, y)
    all_words.add(word)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Add a new falling word periodically
    if random.randint(0, 100) < 5:  # Adjust the frequency of word creation
        add_word()

    # Update and draw the falling words
    all_words.update()
    
    screen.fill((0, 0, 0))  # Fill the screen with a black background
    all_words.draw(screen)

    pygame.display.flip()
    clock.tick(60)  # Set the frame rate to 60 frames per second
