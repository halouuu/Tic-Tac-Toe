#Importing the follwing modules so I can use them in my code
import sys
import pygame
#this is for creating a temporary board used for the AI
import copy
#for the random AI
import random
#This module is used for the console board
import numpy as np
from constants import *
from setting_up import *

#initializes (starts) all pygame modules
pygame.init()

#Choosing between different gamemodes
def Play():
    while True:
        #put the position of the mouse into a variable
        play_mouse_pos = pygame.mouse.get_pos()
        
        #filling the screen 
        screen.fill(BACKGROUND_COLOUR)

        play_text = main_font.render("Choose an option...", True, "white")
        play_rect = play_text.get_rect(center=(300,100))
        
        play_back = Button(None, (300,550), "Go back to main menu :)", "Black", "White")
        play_go = Button(None, (300,250), "Let's Go!", "Black", "White")
        screen.blit(play_text, play_rect)

        #Displaying the text for the play screen. 
        play_body_text_show1 = text_font.render(play_body_text1, True, "Black")
        play_body_text_rect = play_body_text_show1.get_rect(center = (300, 325))
        screen.blit (play_body_text_show1, play_body_text_rect)
        play_body_text_show2 = text_font.render(play_body_text2, True, "Black")
        play_body_text_rect = play_body_text_show2.get_rect(center = (300, 375))
        screen.blit (play_body_text_show2, play_body_text_rect)
        play_body_text_show3 = text_font.render(play_body_text3, True, "Black")
        play_body_text_rect = play_body_text_show3.get_rect(center = (300, 425))
        screen.blit (play_body_text_show3, play_body_text_rect)
        play_body_text_show4 = text_font.render(play_body_text4, True, "Black")
        play_body_text_rect = play_body_text_show4.get_rect(center = (300, 475))
        screen.blit (play_body_text_show4, play_body_text_rect)

        #Changing the colour when the mouse hovers over it
        for button in [play_back, play_go]:
            button.ChangeColour(play_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #Check if clicked on to go to another screen
                if play_back.CheckForInput(play_mouse_pos):
                    main_menu()
                if play_go.CheckForInput(play_mouse_pos):
                    main()
                
        pygame.display.update()

def htp():
    while True:
        htp_mouse_pos = pygame.mouse.get_pos()

        screen.fill(BACKGROUND_COLOUR)

        #Set the heading for the How to Play screen
        htp_text = main_font.render("How do I play?", True, "White")
        htp_rect = htp_text.get_rect(center=(300,100))
        screen.blit(htp_text, htp_rect)

        #Showing the text for the How to Play screen
        htp_body_text_show1 = text_font.render(htp_body_text1, True, "Black")
        htp_body_text_rect = htp_body_text_show1.get_rect(center = (300,200))
        screen.blit(htp_body_text_show1, htp_body_text_rect)
        htp_body_text_show2 = text_font.render(htp_body_text2, True, "Black")
        htp_body_text_rect = htp_body_text_show2.get_rect(center = (300,250))
        screen.blit(htp_body_text_show2, htp_body_text_rect)
        htp_body_text_show3 = text_font.render(htp_body_text3, True, "Black")
        htp_body_text_rect = htp_body_text_show3.get_rect(center = (300,300))
        screen.blit(htp_body_text_show3, htp_body_text_rect)
        htp_body_text_show4 = text_font.render(htp_body_text4, True, "Black")
        htp_body_text_rect = htp_body_text_show4.get_rect(center = (300,350))
        screen.blit(htp_body_text_show4, htp_body_text_rect)

        #A button to go back to the Main Menu
        htp_back = Button(None, (300,550), "Baaaaaack to the Main Menu", "Black", "White")
        htp_back.ChangeColour(htp_mouse_pos)
        htp_back.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if htp_back.CheckForInput(htp_mouse_pos):
                    main_menu()

        pygame.display.update()

def main_menu():
    pygame.display.set_caption("Menu")

    while True:
        screen.fill(BACKGROUND_COLOUR)

        #Get the mouse position
        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = main_font.render("Main Menu", True, "White")
        menu_rect = menu_text.get_rect(center=(300,100))

        #The two buttons to go to other screens
        play_button = Button(None, (300,250),"Let's Play!", ((0,0,0)), "White")
        htp_button = Button(None, (300,350), "How do I play?", ((0,0,0)), "White")

        screen.blit (menu_text, menu_rect)

        for button in [play_button, htp_button]:
            button.ChangeColour(menu_mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.CheckForInput(menu_mouse_pos):
                    Play()
                if htp_button.CheckForInput(menu_mouse_pos):
                    htp()
        
        pygame.display.update()

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
        self.gamemode = 'pvp' #pvp or ai
        #if the game is not over. Game is over when there is a draw or a player wins.
        self.playing = True

    #to show the game board lines
    def show_lines (self):
        #this will paint the screen again when it restarts.
        screen.fill(BACKGROUND_COLOUR)
        
        #vertical lines
        pygame.draw.line(screen, LINE_COLOUR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOUR, (WIDTH - SQUARE_SIZE, 0), (WIDTH - SQUARE_SIZE, HEIGHT), LINE_WIDTH)

        #horizontal lines
        pygame.draw.line(screen, LINE_COLOUR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOUR, (0, HEIGHT - SQUARE_SIZE), (WIDTH, HEIGHT- SQUARE_SIZE), LINE_WIDTH)

    #to connect the console board to the graphic board
    def draw_fig(self, row, col):
        if self.player == 1:
            #draw cross
            
            #starting position for negative line
            start_neg = (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + OFFSET)
            #ending position for negative line
            end_neg = (col * SQUARE_SIZE + SQUARE_SIZE - OFFSET, row * SQUARE_SIZE + SQUARE_SIZE - OFFSET)
            #starting position for positive line
            start_pos = (col * SQUARE_SIZE + OFFSET, row * SQUARE_SIZE + SQUARE_SIZE - OFFSET)
            #ending position for positive line
            end_pos = (col * SQUARE_SIZE + SQUARE_SIZE - OFFSET, row * SQUARE_SIZE + OFFSET)

            pygame.draw.line(screen, CROSS_COLOUR, start_neg, end_neg, CROSS_WIDTH)
            pygame.draw.line(screen, CROSS_COLOUR, start_pos, end_pos, CROSS_WIDTH)

        elif self.player == 2:
            #draw circle
            center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
            pygame.draw.circle(screen , CIRCLE_COLOUR, center, RADIUS, CIRCLE_WIDTH)

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

def gameover():
        pygame.display.flip
        pygame.display.set_caption("Thanks for Playing!")

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
                    if event.key == pygame.K_1: 
                        game.change_gamemode()
    
                    #changing the gamemode to random AI
                    if event.key == pygame.K_2:
                        ai.level = 0

                    #changing the gamemode to minimax AI
                    if event.key == pygame.K_3:
                        ai.level = 1

                    #reseting the game
                    if event.key == pygame.K_4:
                        game.reset()
                        #restarted the game but the board has not been restarted so this is important.
                        board = game.board
                        ai = game.ai

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #event.pos alone will give you postition in pixels but we want it in terms of rol and col
                    pos = event.pos
                    #pos[1] = y-axis
                    row = pos[1] // SQUARE_SIZE
                    #pos[0] = x-axis
                    col = pos[0] // SQUARE_SIZE
                
                    if board.empty_square(row,col) and game.playing:
                        game.make_move(row,col)

                        if game.isover():
                            game.playing = False
                            gameover()

        if game.gamemode == 'ai' and game.player == ai.player and game.playing:
            #update the screen so the player can see the updated screen with the AI move before the AI makes another move.
            pygame.display.flip()

            #AI methods
            #ai.evaluation will return a move in the form of (row,col) which will be saved into 2 variables.
            row,col = ai.eval(board)
            game.make_move(row,col)

            if game.isover():
                game.playing = False
                gameover()
                        
       
        #This updates the display
        pygame.display.update()

#runs main function
#main()
main_menu()