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

def draw_text(text, size, x, y):
    font = pygame.font.Font(FONT_NAME, FONT_SIZE)
    text_surface = font.render(text, True, FONT_COLOUR)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_surface,text_rect)
