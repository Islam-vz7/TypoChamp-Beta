#!/usr/bin/env python3

# set a timer 1 minute each (5 rounds first) 
# longer words (1-3 -> 5 -> 7 -> 
# faster movement after 1 minute (clock) 
# Lower case 1st round 

import pygame
import random
from sys import exit
import sys
from pygame.locals import *
import time

pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("TypoChamp")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)
menu_ground = pygame.image.load("Keyboard.jpg") 

# Set up the font
font = pygame.font.Font(None, 36)

# Define the menu options
menu_options = ["Start Game", "Quit"]

# Initialize variables
selected_option = 0
in_menu = True

# Function to handle starting the game
def start_game():
    print("Starting the game!")

# Function to display the menu
def display_menu():
    #screen.fill(menu_ground)
    screen.blit(menu_ground, (0, 0))

    for i, option in enumerate(menu_options):
        text_color = white if i == selected_option else black
        text_surface = font.render(option, True, text_color)
        text_rect = text_surface.get_rect(center=(width // 2, height // 2 + i * 50))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if in_menu:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Start Game
                        start_game()
                        in_menu = False
                    elif selected_option == 1:  # Quit
                        pygame.quit()
                        sys.exit()

    if in_menu:
        display_menu()
    else:   
    #Defining
      surface_width = 100 #pls review 
      surface_height = 300 #pls review 
      background_colour = ('#176B87')
      level1_words = []
      level2_words = []
      font_size = 36
      font_colour = (255, 255, 255)
      fall_speed = 0.05
      score = 0
      game_over = False

      screen = pygame.display.set_mode((width,height))
      pygame.display.set_caption('TypoChamp')
      clock = pygame.time.Clock() 
      font = pygame.font.Font(None ,font_size)

      seconds, seconds_text = 10, '10'.ljust(0)
      minutes, minutes_text = 10, '10'.rjust(0)
      score_text = '0'.rjust(0)
      playername, name_text = "Playername", "Playername".ljust(0) #Get player name from somewhere
      pygame.time.set_timer(pygame.USEREVENT, 1000)             
                                                                
      #test_font = pygame.font.Font(None, 50) #pls review
      #test_surface = pygame.image.load('') #Photoshop a background pic ? 

      screen.fill(background_colour)

      #Organizing the words according to their length and put them in a list to use later
      with open("words.txt", "+r") as file:
          for line in file:
            word = file.read().splitlines()

            if 1 <= len(word) <= 5:
              level1_words.append(word)

            elif 6 <= len(word) <= 9:
              level2_words.append(word)

      #Timer
      while not game_over:    
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            exit()
          if event.type == pygame.USEREVENT: # Updates the timer, and text to be displayed
            seconds += 1
            seconds_text = str(seconds).rjust(0)
            score_text = str(score).rjust(0)
            if seconds >= 60:
              seconds = 0
              seconds_text = str(seconds).rjust(0)
              minutes += 1
              minutes_text = str(str(minutes)).rjust(0)
            

        pygame.display.update()
        screen.fill(background_colour)                                      #Displaying text
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 30))                #Black bar on top
        screen.blit(font.render(name_text, True, font_colour), (4, 4))      #Playername
        screen.blit(font.render(seconds_text, True, font_colour), (415, 4)) #Seconds
        screen.blit(font.render(":".center(0), True, font_colour), (395, 4)) #Separator
        screen.blit(font.render(minutes_text, True, font_colour), (375, 4)) #Minutes
        screen.blit(font.render(score_text, True, font_colour), (780, 4))   #Score
        pygame.display.flip()
        clock.tick(60)

# Pixel Array: We are using 64-bit python 
# pixel_numbers = pygame.PixelArray.surface
# import math 
# x += math.cos(angle) * amount_to_move
# y += math.sin(angle) * amount_to_move
# import numpy

# capture using typing speed using python code -> if player typed faster, we will show the new words faster (or the new words will move faster)
# def capture_typing_speed(text, time_used):
# words = text.split()
# num_words = len(words)
# seconds = time_used / 60
# words_per_sec 