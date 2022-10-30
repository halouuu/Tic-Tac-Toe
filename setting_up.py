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
main_font = pygame.font.SysFont("Inkfree", 70)
main_font.set_underline(True)
button_font = pygame.font.SysFont("cambria", 35)
text_font = pygame.font.SysFont("georgia", 20)

def draw_text(text, size, x, y):
    font = pygame.font.Font(FONT_NAME, FONT_SIZE)
    text_surface = font.render(text, True, FONT_COLOUR)
    text_rect = text_surface.get_rect()
    text_rect.center = (x,y)
    screen.blit(text_surface,text_rect)

### For the start menu ###
#For the body text in How to Play screen
htp_body_text1 = "Welcome! To play the game, just press on \"Let's play!\""
htp_body_text2 = "If you want to reset the game, just press the r key. If you reset,"
htp_body_text3 = "then everything will go back to default (player vs player)"
htp_body_text4 = ""

#For the body text in the Play screen
play_body_text1 = "The defult game mode is player vs player."
play_body_text2 = "if you want to play against an unbeatable AI: press 1"
play_body_text3 = "if you want to play against the random AI: press 2"
play_body_text4 = "To get started: press \"Let's Go!\""

#This is for creating the button for the menu screen
class Button():
    def __init__ (self, image, pos, text_input, base_colour, hovering_colour):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.base_colour, self.hovering_colour = base_colour, hovering_colour
        self.text_input = text_input
        self.text = button_font.render(self.text_input, True, self.base_colour)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    
    def update (self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
        
    def CheckForInput (self, position):
        if position [0] in range(self.rect.left, self.rect.right) and position [1] in range (self.rect.top, self.rect.bottom):
            return True
        return False

    def ChangeColour (self, position):
        if position [0] in range(self.rect.left, self.rect.right) and position [1] in range (self.rect.top, self.rect.bottom):
            self.text = button_font.render(self.text_input, True, self.hovering_colour)
        else:
            self.text = button_font.render(self.text_input, True, self.base_colour)