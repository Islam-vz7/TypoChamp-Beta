#!/usr/bin/env python3

# set a timer 1 minute each (5 rounds first) 
# longer words (1-3 -> 5 -> 7 -> 
# faster movement after 1 minute (clock) 
# Lower case 1st round 

# ALL YE WHO ENTER ABONDON THY HOPE, FOR THIS PLACE IS STUCK IN-BETWEEN TIME AND SPACE, WHILST OVERFLOWING WITH SHAME AND DISGRACE
# LOL 

import pygame
import random
from sys import exit
import sys
from pygame.locals import *
import time
import math
from math import floor

pygame.init()

# Set up the game window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
# icon = pygame.image.load("icon.png") 
# pygame.display.set_icon(icon)  
pygame.display.set_caption("TypoChamp")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)
purple = ('#5e17eb')

menu_ground = pygame.image.load("TypoChampLogo.png") 

# Set up the font
font = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 42)

# Define the menu options
menu_options = ["Start",  "Scores", "Credits", "Quit"] 
# round_options = ["Keep Challenging", "Give up"]

# Initialize variables
selected_option = 0
in_menu = True

# Function to handle starting the game
def start_game():
    print("Starting the game!")
def open_scores():
    print("Launching the LeaderBoard!")
def open_credits():
    print("Launching the Credits!")

# Function to display the menu
def display_menu():
    #screen.fill(menu_ground)
    screen.blit(menu_ground, (0, 0))

    for i, option in enumerate(menu_options):
        text_color = purple if i == selected_option else black
        text_surface = font.render(option, True, text_color)
        text_rect = text_surface.get_rect(center=(width // 2, height // 2 + i * 50))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()

# Main game loop
# def round_menu(): 
# -> Should we add draw_menu(round_options) 
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
                    if selected_option == 0:  # Start
                        start_game()
                        in_menu = False
                    elif selected_option == 1:  # Scores
                        open_scores()
                        in_menu = False
                    elif selected_option == 2:  # Credits
                        open_credits()
                        in_menu = False
                    elif selected_option == 3:  # Quit
                        pygame.quit()
                        sys.exit()

    if in_menu:
        display_menu()
    #elif :
    
    else:   
    #Defining
      surface_width = 100 
      surface_height = 300  
      background_colour = ('#176B87')
      font_size = 36
      font_colour = (255, 255, 255)
      gravity = 0.2           # How fast a word falls
      word_cooldown = 1.5        # COOLDOWN in between each falling word // Lower = More Words
      word_ttf = word_cooldown # TIME TO FALL
      game_over = False
      input_word = ""

      screen = pygame.display.set_mode((width,height))
      pygame.display.set_caption('TypoChamp')
      clock = pygame.time.Clock() 
      font = pygame.font.Font(None ,font_size)

      words_ons = []  #List of all words on screen
      words_pos = []  #List of all word positions on screen // index 0 is position of word index 0 in words_ons
      words_grv = []  #List of all word fall speeds
      milsec = 1000
      seconds = 0
      minutes = 0
      score, score_text = 0, 'Score: 0'.rjust(30)
      playername, name_text = "Playername", "Playername".ljust(0) #Get player name from somewhere
      the_big_time = (str(minutes) + " : " + str(floor(seconds))).center(0)
      pygame.time.set_timer(pygame.USEREVENT, 10)             
                                                               

      screen.fill(background_colour)

      #Organizing the words according to their length and put them in a list to use later
      def read_words1():
         level1_words = []
         with open("words.txt", "+r") as file:
            for line in file:
              word = line.strip()
              if 1 <= len(word) <= 4:
                level1_words.append(word)
          
         return level1_words
      
      def read_words2():
         level2_words = []
         with open("words.txt", "+r") as file:
            for line in file:
              word = line.strip()
              if len(word) >= 5:
                 level2_words.append(word) 

         return level2_words
      
      level1_words = read_words1()
      level2_words = read_words2()

      
      def spawn_new_word(): #Spawns a new word on screen
        new_word = str(random.choice(level1_words))
        words_ons.append(new_word)
        words_pos.append([random.randint(50, 540), 0])
        words_grv.append((random.randint(1, 10) / 10))
        print(f"New word: {words_ons[-1]}, Position: X:{words_pos[-1][0]} Y:{words_pos[-1][1]}")


      def apply_gravity(): #Shifts all words on screen downwards
         for x in range(0, len(words_pos)):
            words_pos[x][1] += words_grv[x]

      #Timer
      while not game_over:    
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
          if event.type == pygame.USEREVENT: # Updates the timer, and text to be displayed
            word_ttf -= 0.01
            seconds += 0.01
            the_big_time = (str(minutes) + " : " + str(floor(seconds))).center(0)
            apply_gravity()
            if seconds >= 60:
              seconds = 0
              minutes += 1
              the_big_time = (str(minutes) + " : " + str(floor(seconds))).center(0)
            if word_ttf <= 0:
              word_ttf = word_cooldown
              spawn_new_word()
              
        pygame.display.update()
        screen.fill(background_colour)

        #Displaying text
        if(len(words_ons) > 0):
          for x in range(0, len(words_ons)):
            screen.blit(font2.render(words_ons[x], True, font_colour), (words_pos[x][0], words_pos[x][1]))
            
        pygame.draw.rect(screen, (0, 0, 0), (0, 0, 800, 30))                 #Black bar on top
        screen.blit(font.render(name_text, True, font_colour), (4, 4))       #Playername
        screen.blit(font.render(the_big_time, True, font_colour), (360, 4))  #Timer
        screen.blit(font.render(score_text, True, font_colour), (520, 4))    #Score
        pygame.display.flip()
        clock.tick(60)


        #Add ranking board 
        






# Pixel Array: We are using 64-bit python 
# pixel_numbers = pygame.PixelArray.surface
# import math 
# x += math.cos(angle) * amount_to_move
# y += math.sin(angle) * amount_to_move
# import numpy

# capture using typing speed using python code
# def capture_typing_speed(text, time_used):
# words = text.split()
# num_words = len(words)
# seconds = time_used / 60
# words_per_sec = num_words / seconds 
# return words_per_sec

# def main():
  # prompt = "Type faster or you will fall into the river!"
  # print(prompt)

# speed of new words coming down

# if player typed faster, we will show the new words faster (or the new words will move faster
# if words_per_sec >= ___:
# 
# elif 

# UI - enlarge words when player type the words correctly 

# Rectangles: tuples (x, y)  
# Level 1 - stright down
# with open("words.txt", "+r") as file:
# player_surf = file.read() 
# player_rect = player_surf.get_rect(topleft = (x,y))
# Level 2 - straight and then left 
# Level 3 - striaght left right straight 

