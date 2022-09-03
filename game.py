from constants import *
from setting_up import *
from board import *
from AI import *

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
