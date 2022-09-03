import pygame
from constants import *
from setting_up import *

class EndMenu():
    def gameover():
        pygame.display.flip
        pygame.time.wait(3000)
        draw_text("Thanks for playing :)", 64, 200, 200)