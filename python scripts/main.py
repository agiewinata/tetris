"""
The main.py is responsible for actually running all 
the logic that has been set for the game. This class 
would run the main loop of the main game, draw all 
of its element, and let user interact with the game.
"""

import pygame
import sys
from grid import Grids
from colours import Colours
from game import Game

pygame.init()

#initialising some key variable for the main method
font = pygame.font.Font(None, 40)
score_surface = font.render("Score", True, Colours.white)
next_surface = font.render("Next", True, Colours.white)
game_over_surface = font.render("Game Over! press r to restart!", True, Colours.white)

score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

canvas = (500,620)
display = pygame.display.set_mode(canvas)
frame = 100

pygame.display.set_caption("Tetris Game")

clock = pygame.time.Clock() 
game_grid = Grids() 
game = Game()

game_update = pygame.USEREVENT #userevetn create an a custom veent

default_trigger = 500
fastest_triger = 150
increment_speed = 50
last_trigger = default_trigger
pygame.time.set_timer(game_update, default_trigger) # this will trigger the cusom event onvce evry 500 ms

# main loop
while True:
    #.event.get() would make get all the evnt pygame recognise and put them in a list
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
        
        # the snippet that control the keys
        if event.type == pygame.KEYDOWN:
            if game.game_over == True and event.key == pygame.K_r:
                game.game_over = False
                game.reset_game()
                pygame.time.set_timer(game_update, default_trigger)
            else:
                if event.key == pygame.K_s and game.game_over == False: 
                    game.move_down()
                    game.update_score(0,1)
                if event.key == pygame.K_a and game.game_over == False: 
                    game.move_left()
                if event.key == pygame.K_w and game.game_over == False: 
                    game.rotation()
                if event.key == pygame.K_d and game.game_over == False: 
                    game.move_right()
                
        if event.type == game_update and game.game_over == False:
            game.move_down()

        #make the pace faster every 150 points
        new_trigger = default_trigger - (game.score//150) * increment_speed
        new_trigger = max(new_trigger, fastest_triger)
        if new_trigger != last_trigger:
            pygame.time.set_timer(game_update, new_trigger)
        last_trigger = new_trigger

    # the part responsible for drawing all the elements
    score_value_surface = font.render(str(game.score), True, Colours.white)
    display.fill(Colours.dark_blue)
    display.blit(score_surface, (365, 20, 50, 50))
    display.blit(next_surface, (375, 180, 50, 50))
    
    pygame.draw.rect(display, Colours.light_blue, score_rect)
    display.blit(score_value_surface, 
                score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(display, Colours.light_blue, next_rect)
    game_grid.draw(display)

    if game.game_over: 
        display.blit(game_over_surface, game_over_surface.get_rect(center=(canvas[0]//2, canvas[1]//2)))
    else:
        game.draw_elements(display)

    pygame.display.update()
    clock.tick(frame)