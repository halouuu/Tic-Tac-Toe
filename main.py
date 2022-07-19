#Importing the follwing modules so I can use them in my code
import sys
from turtle import back, pos
import pygame
#This module is used for the console board
import numpy as np
from constants import *

#initializes (starts) all pygame modules
pygame.init()

#Setting up the screen
#setting up the dimensions of the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#setting up the dimensions of the screen (will probably change later)
pygame.display.set_caption("Sophia's L3 Project - AI Tic Tac Toe <3")
#Putting a background colour
screen.fill(background_colour)

class Board:

    def __init__ (self):
        self.squares = np.zeros ((ROWS, COLS))
        #zeros = empty squares

    def mark_square (self, row, col, player):
        #there will be two players: 1, 2. When a square is marked, the square on console board will not be zero anymore, it will be replaced with bthe player number (1 or 2)
        self.squares[row][col] = player

    def empty_square(self, row, col):
        #if this is true, then the square is empty
        return self.squares[row][col] == 0

class Game:

    #Init method - allows the class to initialize the attributes of the class
    #parameter is self because it access the methods and attributes
    def __init__ (self):
        #creating the console board to help with logic
        self.board = Board()
        #player 1 = crosses
        #player 2 = noughts (circles)
        self.player = 1
        self.show_lines()

    #to show the game board lines
    def show_lines (self):
        #vertical lines
        pygame.draw.line(screen, line_colour, (square_size, 0), (square_size, HEIGHT), line_width)
        pygame.draw.line(screen, line_colour, (WIDTH - square_size, 0), (WIDTH - square_size, HEIGHT), line_width)

        #horizontal lines
        pygame.draw.line(screen, line_colour, (0, square_size), (WIDTH, square_size), line_width)
        pygame.draw.line(screen, line_colour, (0, HEIGHT - square_size), (WIDTH, HEIGHT- square_size), line_width)

    #to connect the console board to the graphic board
    def draw_fig(self, row, col):
        if self.player == 1:
            #draw cross
            
            #starting position for negative line
            start_neg = (col * square_size + offset, row * square_size + offset)
            #ending position for negative line
            end_neg = (col * square_size + square_size - offset, row * square_size + square_size - offset)
            #starting position for positive line
            start_pos = (col * square_size + offset, row * square_size + square_size - offset)
            #ending position for positive line
            end_pos = (col * square_size + square_size - offset, row * square_size + offset)

            pygame.draw.line(screen, cross_colour, start_neg, end_neg, cross_width)
            pygame.draw.line(screen, cross_colour, start_pos, end_pos, cross_width)

        elif self.player == 2:
            #draw circle
            center = (col * square_size + square_size // 2, row * square_size + square_size // 2)
            pygame.draw.circle(screen , circle_colour, center, radius, circle_width)

    #to switch players
    def next_turn(self):
        self.player = self.player % 2 + 1
        ''' example:
            if player = 1:
                1 % 1 + 1 = 2
            if player = 2:
                2 % 2 + 1 = 1
        '''

#The main function, will include main loop
def main():
    
    #game object to call game class
    game = Game()
    #this variable just makes my life easier so I don't have to type game.board everytime
    board = game.board

    while True:

        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    #deintiallizes (quits) all pygame modules
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #event.pos alone will give you postition in pixels but we want it in terms of rol and col
                    pos = event.pos
                    #pos[1] = y-axis
                    row = pos[1] // square_size
                    #pos[0] = x-axis
                    col = pos[0] // square_size
                
                    if board.empty_square(row,col):
                        board.mark_square(row,col,game.player)
                        game.draw_fig(row,col)
                        game.next_turn()
                        

       
        #This updates the display
        pygame.display.update()

#runs main function
main ()