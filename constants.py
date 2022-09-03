import pygame

#Dimensions of screen
WIDTH = 600
HEIGHT = 600

#Game board
ROWS = 3
COLS = 3

# 3 divided by 3 = 1 = square size
SQUARE_SIZE = WIDTH // COLS
#Colour (will be changed later on)
BACKGROUND_COLOUR = ((123,123,123))
#lines
LINE_COLOUR = ((1,2,3))
LINE_WIDTH = 15

#circle (noughts)
CIRCLE_WIDTH = 15
RADIUS = SQUARE_SIZE // 4
CIRCLE_COLOUR = ((123, 132, 231))

#cross
CROSS_COLOUR = ((231,132,123))
CROSS_WIDTH = 20
OFFSET = 50

#fonts
FONT_NAME = pygame.font.get_default_font()
FONT_SIZE = 15
FONT_COLOUR = ((231,132,123))

#menu
MENU_COLOUR = ((255,255,255))