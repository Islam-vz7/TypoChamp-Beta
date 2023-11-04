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

screen_width = 800
screen_height = 600
surface_width = 100 #pls review 
surface_height = 300 #pls review 
background_colour = ('#176B87')
level1_words = []
level2_words = []
font_size = 36
fall_speed = 0.05

screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('TypoChamp')
clock = pygame.time.Clock()
font = pygame.font.Font(None,font_size)

# test_font = pygame.font.Font(None, 50) #pls review
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

#Words falling and reaching the ground
def falling_words():
  words_select_level1 = random.choice(level1_words)
  x = random.randint(0, screen_width - font_size)
  y = 0
  return {"word": words_select_level1, "x": x, "y": y}

#Creating a timer 
while True:
  elapsed_time = int(time.time() - time.time())
  minutes, seconds = divmod(elapsed_time, 60)
  time_str = f"Time: {minutes:02d}:{seconds:02d}"
  
  timer_text = font.render(time_str, True, (0, 0, 0))
  screen.blit(timer_text, (600, 10))

  start_time = time.time()


  pygame.display.flip()
  pygame.time.Clock().tick(60)
  break

while True:    
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit() 

  pygame.display.update()
