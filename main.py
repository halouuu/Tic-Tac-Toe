#Importing the follwing modules so I can use them in my code
import sys
import pygame
from constants import *
from setting_up import *
from game import *

#initializes (starts) all pygame modules
pygame.init()

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
                    row = pos[1] // SQUARE_SIZE
                    #pos[0] = x-axis
                    col = pos[0] // SQUARE_SIZE
                
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