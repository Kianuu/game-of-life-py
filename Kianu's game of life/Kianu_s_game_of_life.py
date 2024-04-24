"""
Kianu's game of life! 

Hello, my name is Kianu and this is my take on Conway's Game of Life. 

The rules are simple:

    1. Any cell with one or less neighbors, they will die, as if by solitude
    2. Any cell with four or more neighbors dies, as if by overpoulation
    3. Any cell with two or three neighbors will live on to next generation
    4. Any dead cell with exactly 3 live neighbors becomes a live cell, as if by reproduction
"""
import pygame


game_chars = ["_","*", "X"]
map_size = {'x':64, 'y':64}




def main():
    print("Hello player, welcome to the Game of Life.\n")
    game_mode = input("The rules are quite simple.\n\n \
                              If you would like to view them press 1. \n \
                              If you would like to begin the simulation of life, press 2. \n \
                              If you would like to view stats, press 3")
    
    
    
    # initialize game window and main loop
    if game_mode == '2':
        while game_mode == 0:
            ## event poll 
            # pygame initialization
            pygame.init()
            display = pygame.display.set_mode((600, 400))
            clock = pygame.time.Clock()
            dt = 0
        