from constants import *
import pygame

pygame.init()

#Setting up the screen
#setting up the dimensions of the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#setting up the dimensions of the screen (will probably change later)
pygame.display.set_caption("Sophia's L3 Project - AI Tic Tac Toe <3")
#Putting a background colour
screen.fill(BACKGROUND_COLOUR)