from constants import * 
from setting_up import *
#This module is used for the console board
import numpy as np
import pygame

pygame.init()

class Board:

    def __init__ (self):
        self.squares = np.zeros ((ROWS, COLS))
        #zeros = empty squares
        self.empty_squares = self.squares
        #a list of empty of empty squares
        self.marked_squares = 0
        #It will be 0 at the start because there will be no markled squares at the start of the game.

    def final_state(self, show = False):
        #return 0 if there is no win yet, but it does not mean that there is a draw.
        #return 1 if player 1 wins.
        #return 2 if player 2 wins

        #vertical wins
        #need to loop through all columns.
        for col in range (COLS):
            #this checks if each figure in a column is the same. It can not = 0 because it has to be a marked square. If that is not added in then it will also check empty columns as well. Which would not result in a win.
            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:
                if show:
                    #this will be the colour of the winning line
                    colour = CIRCLE_COLOUR if self.squares[0][col] == 2 else CROSS_COLOUR
                    #initial position
                    iPos = (col * SQUARE_SIZE + SQUARE_SIZE // 2, 20)
                    #final position
                    fPos = (col * SQUARE_SIZE + SQUARE_SIZE // 2, HEIGHT - 20)
                    pygame.draw.line(screen, colour, iPos,fPos, LINE_WIDTH)
                #we want it to return anyone of the squares because they are all the same number. I just chose the first one. 
                #eg. 1 = 1 = 1 != 0, we return 1 when player one wins.
                return self.squares[0][col]

        for row in range (ROWS):
            #this checks if each figure in a row is the same. It can not = 0 because it has to be a marked square. If that is not added in then it will also check empty columns as well. Which would not result in a win.
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    #this will be the colour of the winning line
                    colour = CIRCLE_COLOUR if self.squares[row][0] == 2 else CROSS_COLOUR
                    #initial position
                    iPos = (20, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                    #final position
                    fPos = (WIDTH - 20, row * SQUARE_SIZE + SQUARE_SIZE // 2)
                    pygame.draw.line(screen, colour, iPos,fPos, LINE_WIDTH)
                #we want it to return anyone of the squares because they are all the same number. I just chose the first one. 
                #eg. 1 = 1 = 1 != 0, we return 1 when player one wins.
                return self.squares[row][0]

        #diagonal wins
        #negative win
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                colour = CIRCLE_COLOUR if self.squares[1][1] == 2 else CROSS_COLOUR
                #initial position
                iPos = (20,20)
                #final position
                fPos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(screen, colour, iPos, fPos, CROSS_WIDTH)
            return self.squares[0][0]

        #positve win
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                #Colour of the winning player
                colour = CIRCLE_COLOUR if self.squares[1][1] == 2 else CROSS_COLOUR
                #initial position
                iPos = (20,HEIGHT - 20)
                #final position
                fPos = (WIDTH - 20, 20)
                pygame.draw.line(screen, colour, iPos, fPos, CROSS_WIDTH)
            return self.squares[0][0]

        #we want to return 0 if there is no win yet so if non of the above if statements are true, we return 0.
        return 0


    def mark_square (self, row, col, player):
        #there will be two players: 1, 2. When a square is marked, the square on console board will not be zero anymore, it will be replaced with the player number (1 or 2)
        self.squares[row][col] = player
        #this will increase the amount of marked squares which will help us know when the board is full
        self.marked_squares += 1

    def empty_square(self, row, col):
        #if this is true, then the square is empty
        return self.squares[row][col] == 0

    def isfull(self):
        return self.marked_squares == 9
        #if the marked_squares = 9, the board is full, so the function is true.

    def isempty(self):
        return self.marked_squares == 0
        #if the marked_squares = 0, the board is empty, so the function is true.

    def get_empty_squares (self):
        #empty squares will be a list which co-ordinates will be appended to.
        empty_squares = []

        #classic double for loop
        for row in range(ROWS):
            for col in range(COLS):
                #if a square is empty, it will get appended into the empty squares list.
                if self.empty_square(row,col):
                    empty_squares.append((row,col))
            
        return empty_squares
