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
icon = pygame.image.load("icon.png") 
pygame.display.set_icon(icon)  
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
font3 = pygame.font.Font(None, 52)

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
    elif selected_option == 2:
      pass
    elif selected_option == 1:
       pass
    
    else:   
    #Defining
      surface_width = 100 
      surface_height = 300  
      background_colour = (35, 35, 35)
      font_size = 36
      font_colour = (255, 255, 255)
      gravity = 0.2           # How fast a word falls
      gravity_cd = 10
      gravity_cdm = 10
      word_cooldown = 2.0        # COOLDOWN in between each falling word // Lower = More Words
      word_ttf = word_cooldown # TIME TO FALL
      game_over = False
      input_word = ""
      score = 0

      screen = pygame.display.set_mode((width,height))
      pygame.display.set_caption('TypoChamp')
      clock = pygame.time.Clock() 
      font = pygame.font.Font(None ,font_size)

      level_1_et = 1  #On which minute level 1 ends
      level_2_et = 2  #On which minute level 2 ends
      level_3_et = 3  #On which minute level 3 ends
      
      words_ons = []  #List of all words on screen
      words_pos = []  #List of all word positions on screen // index 0 is position of word index 0 in words_ons
      words_grv = []  #List of all word fall speeds
      words_fnt = []  #List of all word fonts // each word has own custom font
      words_clr = []  #List of all word colors
 
      milsec = 1000
      seconds = 0
      minutes = 0
      #score, score_text = 0, 'Score: 0'.rjust(30)
      playername, name_text = "SOURCE", "SOURCE".ljust(0) #Get player name from somewhere
      the_big_time = (str(minutes) + " : " + str(floor(seconds))).center(0)
      pygame.time.set_timer(pygame.USEREVENT, 10)             
                                                               

      screen.fill(background_colour)

      def END_SCREEN_ITS_OVER(playername, score):
         scoreboard = open("data.txt", "a")
         scoreboard.write(f"\n{playername}, {score}")
         scoreboard.close()

      #Organizing the words according to their length and put them in a list to use later
      def read_words1():
         level1_words = []
         with open("words.txt", "+r") as file:
            for line in file:
              word = line.strip()
              if 1 <= len(word) <= 6:
                level1_words.append(word)
          
         return level1_words
      
      def read_words2():
         level2_words = []
         with open("words.txt", "+r") as file:
            for line in file:
              word = line.strip()
              if 7 <= len(word) <= 10:
                 level2_words.append(word) 

         return level2_words
      
      def read_words3():
         level3_words = []
         with open("words.txt", "+r") as file:
            for line in file:
              word = line.strip()
              if  len(word) >= 11:
                 level3_words.append(word) 

         return level3_words

      level1_words = read_words1()
      level2_words = read_words2()
      level3_words = read_words3()

      
      def spawn_new_word(): #Spawns a new word on screen
        if minutes < level_1_et:
          new_word = str(random.choice(level1_words))
          fnt = pygame.font.Font(None, 44)
          
        elif minutes < level_2_et:
          ch = random.randint(0, 1)
          if ch == 0:
            new_word = str(random.choice(level1_words))
            fnt = pygame.font.Font(None, 44)
          if ch == 1:
            new_word = str(random.choice(level2_words))
            fnt = pygame.font.Font(None, 38)
            
        elif minutes < level_3_et:
          ch = random.randint(0, 2)
          if ch == 0:
            new_word = str(random.choice(level1_words))
            fnt = pygame.font.Font(None, 44)
          if ch == 1:
            new_word = str(random.choice(level2_words))
            fnt = pygame.font.Font(None, 38)
          if ch == 2:
            new_word = str(random.choice(level3_words))
            fnt = pygame.font.Font(None, 34)
        
        cl = random.randint(100, 255)
        clr = (cl, cl, cl)
        grv = gravity
        words_ons.append(new_word)
        words_pos.append([random.randint(50, 540), 0])
        words_grv.append(grv)
        words_fnt.append(fnt)
        words_clr.append(clr)
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
          elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
              input_word = input_word[:-1]
            elif event.key == pygame.K_RETURN:
                for index in range(0, len(words_ons) - 1):
                   if input_word == words_ons[index]:
                      del words_ons[index]
                      del words_pos[index]
                      del words_grv[index]
                      del words_fnt[index]
                      del words_clr[index]
                      score += len(input_word)
                input_word = ""
            elif event.key in range(97,123):
              input_word += event.unicode

          if event.type == pygame.USEREVENT: # Updates the timer, and text to be displayed
            if minutes >= 3:
               END_SCREEN_ITS_OVER(playername, score)
            word_ttf -= 0.01
            gravity_cd -= 0.01
            seconds += 0.01
            the_big_time = (str(minutes) + " : " + str(floor(seconds))).center(0)
            apply_gravity()

            for index in range(0, len(words_ons) - 1):
               if words_pos[index][1] >= 600:
                      del words_ons[index]
                      del words_pos[index]
                      del words_grv[index]
                      del words_fnt[index]
                      del words_clr[index]
                      break
               
            if gravity_cd <= 0:
               gravity_cd = gravity_cdm
               gravity += 0.05
               word_cooldown -= 0.15
            if word_cooldown < 0.30:
               word_cooldown = 0.30
            if seconds >= 60:
              seconds = 0
              minutes += 1
              the_big_time = (str(minutes) + " : " + str(floor(seconds))).center(0)
            if word_ttf <= 0:
              word_ttf = word_cooldown
              spawn_new_word()
              
        pygame.display.update()
        screen.fill(background_colour)

        #Bottom Gradient draw start
        hhh = 520
        ccc = 35
        rrr = 0
        zzz = 0
        for i in range(0, 90):
          pygame.draw.rect(screen, (ccc + int(rrr), ccc + zzz, ccc + zzz), (0, hhh, 800, 1))
          hhh += 1
          rrr += 0.5
          zzz = int(rrr / 2)
        #Bottom Gradient draw end

        #Displaying text
        if(len(words_ons) > 0):
          for x in range(0, len(words_ons)):
            screen.blit(words_fnt[x].render(words_ons[x], True, words_clr[x]), (words_pos[x][0], words_pos[x][1]))
            
        pygame.draw.rect(screen, (25, 25, 25), (0, 0, 800, 35))
        screen.blit(font.render(name_text, True, font_colour), (650, 5))       #Playername
        screen.blit(font.render(the_big_time, True, font_colour), (360, 5))  #Timer
        screen.blit(font.render(f"Score: {score}", True, font_colour), (4, 4))    #Score
        screen.blit(font3.render(input_word.center(128), True, (255, 0, 0)), (width // 2 - 660, height -50)) #Input

        pygame.display.flip()
        clock.tick(60)


# #Add ranking board 
#                           ## Initialize an empty scoreboard
#                     scoreboard = {}

#                     def add_score(player, score):
#                         """Add a player's score to the scoreboard."""
#                         if player in scoreboard:
#                             scoreboard[player] += score
#                         else:
#                             scoreboard[player] = score

#                     def display_scoreboard():
#                         """Display the current scoreboard."""
#                         print("----- Scoreboard -----")
#                         for player, score in scoreboard.items():
#                             print(f"{player}: {score} points")
#                         print("----------------------")

#                     # Main game loop
#                     while True:
#                         player_name = input("Enter your name (or 'quit' to exit): ")

#                         if player_name.lower() == 'quit':
#                             break

#                         score = int(input("Enter your score: "))

#                         add_score(player_name, score)
#                         display_scoreboard()

#                     print("Game over! Final scoreboard:")
#                     display_scoreboard() #
          
# This code defines a simple word typing game scoreboard using a dictionary to store player scores. Players can enter their names and scores, and the add_score function keeps track of their scores. The display_scoreboard function prints the current scoreboard. The main game loop continues until the player enters 'quit'. Once the game is over, the final scoreboard is displayed. You can expand and modify this code to suit the specific requirements of your word typing game. #

        






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

