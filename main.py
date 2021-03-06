#Importing the follwing modules so I can use them in my code
import sys
import pygame
#This module is used for the console board
import numpy as np
#for the random AI
import random
#this is for creating a temporary board used for the AI
import copy
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
                    colour = circle_colour if self.squares[0][col] == 2 else cross_colour
                    #initial position
                    iPos = (col * square_size + square_size // 2, 20)
                    #final position
                    fPos = (col * square_size + square_size // 2, HEIGHT - 20)
                    pygame.draw.line(screen, colour, iPos,fPos, line_width)
                #we want it to return anyone of the squares because they are all the same number. I just chose the first one. 
                #eg. 1 = 1 = 1 != 0, we return 1 when player one wins.
                return self.squares[0][col]

        for row in range (ROWS):
            #this checks if each figure in a row is the same. It can not = 0 because it has to be a marked square. If that is not added in then it will also check empty columns as well. Which would not result in a win.
            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:
                if show:
                    #this will be the colour of the winning line
                    colour = circle_colour if self.squares[row][0] == 2 else cross_colour
                    #initial position
                    iPos = (20, row * square_size + square_size // 2)
                    #final position
                    fPos = (WIDTH - 20, row * square_size + square_size // 2)
                    pygame.draw.line(screen, colour, iPos,fPos, line_width)
                #we want it to return anyone of the squares because they are all the same number. I just chose the first one. 
                #eg. 1 = 1 = 1 != 0, we return 1 when player one wins.
                return self.squares[row][0]

        #diagonal wins
        #negative win
        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:
            if show:
                colour = circle_colour if self.squares[1][1] == 2 else cross_colour
                #initial position
                iPos = (20,20)
                #final position
                fPos = (WIDTH - 20, HEIGHT - 20)
                pygame.draw.line(screen, colour, iPos, fPos, cross_width)
            return self.squares[0][0]

        #positve win
        if self.squares[2][0] == self.squares[1][1] == self.squares[0][2] != 0:
            if show:
                colour = circle_colour if self.squares[1][1] == 2 else cross_colour
                #initial position
                iPos = (20,HEIGHT - 20)
                #final position
                fPos = (WIDTH - 20, 20)
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
                if self.empty_squares(row,col):
                    empty_squares.append((row,col))

        return empty_squares

class AI:
    #there will be 3 levels:
        # 0 = random AI: the ai will just go whereever, no strategy involved.
        # 1 = unbeatable AI: the ai will use the minimax algorithm, will never lose.
        # 2 = PVP: 2 players taking turns. Standard tic-tac-toe.
    
    #defult level is 0 (random AI), defult player is 2 (noughts)
    def __init__(self, level = 1, player = 2):
        self.level = level
        self.player = player

    def random(self, board):
        #creating a new list. This function will return all of the empty squares.
        empty_squares = board.get_empty_squares()
        #the move that the AI will make.
        index = random.randrange(0,len(empty_squares))

        #it will return in form of (row,col)
        return empty_squares[index]

    #the board is the board that the algorithm is analysing. Maximising utilizes the minimax algorithm, will return true or false.
    #AI is player two and is trying to minimize because maximising is false. Ref. evaluation function.
    def minimax(self, board, maximising):
        #we need to check terminal cases
        case = board.final_state()

        #player 1 wins
        if case == 1:
            #it returns evaluation, best move
            return 1, None

        #player 2 wins
        if case == 2:
            #it returns evaluation, best move
            return -1, None
        
        #draw
        elif board.isfull():
            #it returns evaluation, best move
            return 0, None

        if maximising:
            #what the maximising player is getting from the board. It will start as any number < -1.
            max_eval = -2
            best_move = None
            #this will be a list in the form (row,col)
            empty_squares = board.get_empty_squares()

            for (row,col) in empty_squares:
                #this creates a temporary board of the orginal board. We want to use a temporary board so it does not affect the main board. The AI needs to test to get the best move.
                temp_board = copy.deepcopy(board)
                #this will mark the temporary board
                temp_board.mark_square(row,col, 1)
                #this time it will use temp_board as the board instead of main_board. It will return an evaluation and a best move.
                #we just want the evaluation, because the (row,col) will be the move which leads to the evaluation.
                #[0] is the first position which will be the evaluation.
                eval = self.minimax(temp_board, False)[0]
                #need to check if the evalution is greater than max_eval (defult is -2). 
                #The evaluation can only be -1, 0, 1. Therefore, the evaluation will always be greater than the max_eval.
                if eval > max_eval:
                    max_eval = eval
                    #this is the move that lead to the evaluation
                    best_move = (row, col)

            return max_eval, best_move

        #this is the AI: trying to not maximise.
        elif not maximising:
            #what the minimising player is getting from the board. It will start as any number >1.
            min_eval = 2
            best_move = None
            #this will be a list in the form (row,col)
            empty_squares = board.get_empty_squares()

            for (row,col) in empty_squares:
                #this creates a temporary board of the orginal board. We want to use a temporary board so it does not affect the main board. The AI needs to test to get the best move.
                temp_board = copy.deepcopy(board)
                #this will mark the temporary board
                temp_board.mark_square(row,col, self.player)
                #this time it will use temp_board as the board instead of main_board. It will return an evaluation and a best move.
                #we just want the evaluation, because the (row,col) will be the move which leads to the evaluation.
                #[0] is the first position which will be the evaluation.
                eval = self.minimax(temp_board, True)[0]
                #need to check if the evalution is less than min_eval (defult is 2). 
                #The evaluation can only be -1, 0, 1. Therefore, the evaluation will always be less than the min_eval.
                if eval < min_eval:
                    min_eval = eval
                    #this is the move that lead to the evaluation
                    best_move = (row, col)

            return min_eval, best_move

    def eval(self, main_board):
        if self.level == 0:
            #random choice
            eval = 'random'
            move = self.random(main_board)
        else:
            #minimax algorithm
            #will return evaluation and move. 
            eval, move = self.minimax(main_board, False)
    
        print (f"AI has chosen to mark the square in position {move} with an evaluation of {eval}")

        #it will return in form of (row,col)
        return move 

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
        self.ai = AI()
        #defult gamemode
        self.gamemode = 'ai' #pvp or ai
        #if the game is not over. Game is over when there is a draw or a player wins.
        self.running = True

    #to show the game board lines
    def show_lines (self):
        #this will paint the screen again when it restarts.
        screen.fill(background_colour)
        
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

    def make_move(self, row, col):
        #mark the square so we know it is not empty
        self.board.mark_square(row, col, self.player)
        #draw the figure so that the player knows where the other player chose.
        self.draw_fig(row,col)
        #switch turns
        self.next_turn()
    
    def next_turn(self):
        self.player = self.player % 2 + 1
        ''' example:
            if player = 1:
                1 % 1 + 1 = 2
            if player = 2:
                2 % 2 + 1 = 1
        '''

    def change_gamemode(self):
        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'

    def isover(self):
        #if the final_state != 0, then that means that someone has won.
        #if the board is full, then there is a draw.
        #if either of those are true then it will return true.
        return self.board.final_state(show = True) != 0 or self.board.isfull()

    def reset (self):
        #this just restarts all of the attributes to all defult values.
        self.__init__()

#The main function, will include main loop
def main():
    
    #game object to call game class
    game = Game()
    #these variables just makes my life easier so I don't have to type game.board etc. everytime
    board = game.board
    ai = game.ai

    while True:

        for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    #deintiallizes (quits) all pygame modules
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    #changing the gamemode to pvp
                    if event.key == pygame.K_g: 
                        game.change_gamemode()
                    
                    #changing the gamemode to random AI
                    if event.key == pygame.K_0:
                        ai.level = 0

                    #changing the gamemode to minimax AI
                    if event.key == pygame.K_1:
                        ai.level = 1

                    #reseting the game
                    if event.key == pygame.K_r:
                        game.reset()
                        #restarted the game but the board has not been restarted so this is important.
                        board = game.board
                        ai = game.ai

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #event.pos alone will give you postition in pixels but we want it in terms of rol and col
                    pos = event.pos
                    #pos[1] = y-axis
                    row = pos[1] // square_size
                    #pos[0] = x-axis
                    col = pos[0] // square_size
                
                    if board.empty_square(row,col) and game.running:
                        game.make_move(row,col)

                        if game.isover():
                            game.running = False

        if game.gamemode == 'ai' and game.player == ai.player and game.running:
            #update the screen so the player can see the updated screen with the AI move before the AI makes another move.
            pygame.display.update()

            #AI methods
            #ai.evaluation will return a move in the form of (row,col) which will be saved into 2 variables.
            row,col = ai.eval(board)
            game.make_move(row,col)

            if game.isover():
                game.running = False
                        
       
        #This updates the display
        pygame.display.update()

#runs main function
main ()