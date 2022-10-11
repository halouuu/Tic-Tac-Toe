from constants import *
import pygame

pygame.init()

#Setting up the screen
#setting up the dimensions of the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#setting up the dimensions of the screen
pygame.display.set_caption("Sophia's L3 Project - AI Tic Tac Toe <3")
#Putting a background colour
screen.fill(BACKGROUND_COLOUR)
#font
main_font = pygame.font.SysFont("cambria", 50)

def draw_text(text, size, x, y):
    font = pygame.font.Font(FONT_NAME, FONT_SIZE)
    text_surface = font.render(text, True, FONT_COLOUR)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_surface,text_rect)

### For the start menu ###

#know if the mouse is hovering over a button or not
mouse_pos = pygame.mouse.get_pos()

class Button():
    def __init__ (self, image, x_pos, y_pos, text_input):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    
    def update (self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect_)
        
    def CheckForInput (self, position):
        if position [0] in range(self.rect.left, self.rect.right) and position [1] in range (self.rect.top, self.rect.bottom):
            print ("button press")

button_surface = pygame.image.load("Resources//Rectangle.png")