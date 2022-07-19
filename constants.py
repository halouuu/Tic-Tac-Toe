#Dimensions of screen
WIDTH = 600
HEIGHT = 600

#Game board
ROWS = 3
COLS = 3
# 3 divided by 3 = 1 = square size
square_size = WIDTH // COLS
#Colour (will be changed later on)
background_colour = ((123,123,123))
#lines
line_colour = ((1,2,3))
line_width = 15

#circle (noughts)
circle_width = 15
radius = square_size // 4
circle_colour = ((123, 132, 231))

#cross
cross_colour = ((231,132,123))
cross_width = 20
offset = 50