
import pygame
import subprocess, os 
import time
## Public code rules :)



game_chars = ["_","*", "X"]
map_size = {'x':64, 'y':64}


## Some constants 

main_rules = """\
Kianu's game of life! \n\n\
Hello, my name is Kianu and this is my take on Conway's Game of Life. \n\
The rules are simple: \n\n\
    1. Any cell with one or less neighbors, they will die, as if by solitude\n\
    2. Any cell with four or more neighbors dies, as if by overpoulation\n\
    3. Any cell with two or three neighbors will live on to next generation\n\
    4. Any dead cell with exactly 3 live neighbors becomes a live cell, as if by reproduction\n\n\
"""

main_menu = "The rules are quite simple.\n\n \
If you would like to view them press 1. \n \
If you would like to begin the simulation of life, press 2. \n \
If you would like to view stats, press 3\nEnter option: "



def main():
    print("Hello player, welcome to the Game of Life.\n")

    
    
    game_mode = input(main_menu)
        # want create one initial loop here as a main menu 
    
    running = True
    
    # run a loop within a loop? sounds stupid but w/e 

    while running:
        
        # then a central case manager for 1 - 3 
        if game_mode == 'e':
            print(main_rules)
            print("\nPress 1 to view the rules, 2 to play, 3 for stats and X to exit: \n")
            game_mode = input("Enter your choice: \n")
            

        elif game_mode == '1':
            
            game_mode = input("\nPress 2 to play, 3 for stats and X to exit: \n")           
            continue
        
        elif game_mode == '2':
            pygame.init()
            screen = pygame.display.set_mode((1200, 900))
            player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

            clock = pygame.time.Clock()
            dt = 0
            screen.fill("dark green")
            print("If you want to quit: press E to return to main menu")
            while game_mode == '2':
                ## event poll game selected --> render screen 
                # pygame initialization
                screen.fill("dark green")
                pygame.draw.circle(screen, "red", player_pos, 30)
                pygame.display.flip()
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w]:
                    player_pos.y -= 300 * dt
                if keys[pygame.K_s]:
                    player_pos.y += 300 * dt
                if keys[pygame.K_a]:
                    player_pos.x -= 300 * dt
                if keys[pygame.K_d]:
                    player_pos.x += 300 * dt
                if keys[pygame.K_e]:
                    ## Exit from game mode and return to main menu...
                    ## not working for now - fix later 
                    game_mode = 'e'
                    for i in range(5):
                        os.system('cls')
                        print("Loading main menu.")
                        time.sleep(0.5)
                        
                        os.system('cls')
                        print("Loading main menu..")
                        time.sleep(0.5)                        

                        os.system('cls')
                        print("Loading main menu...")
                        time.sleep(0.5)                        
                    




                dt = clock.tick(60) / 1000
                

                



main()