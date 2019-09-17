import sys

import pygame

def run_game():
    #initialize pygame and screen and set caption
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")

    #start main loop of the game. if True, which it indefinitely is, keep the game on. 
    while True:
       
        #watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #the only way to shut it off is if event QUIT happens
                sys.exit()
       
        #this makes makes the most recently drawn screen visible
        pygame.display.flip()

#run the game by calling it
run_game()
