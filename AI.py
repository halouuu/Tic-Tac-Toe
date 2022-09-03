#this is for creating a temporary board used for the AI
import copy
#for the random AI
import random
from constants import *
from setting_up import *

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
