import pygame
import sys
from grid import Grids
from colours import Colours
from game import Game

pygame.init()

font = pygame.font.Font(None, 40)
score_surface = font.render("Score", True, Colours.white)
next_surface = font.render("Next", True, Colours.white)
game_over_surface = font.render("Game Over!", True, Colours.white)
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

canvas = (500,620)
display = pygame.display.set_mode(canvas)
frame = 30

pygame.display.set_caption("Tetris Game")

clock = pygame.time.Clock() #initialise a Clock() object
game_grid = Grids() 
game_grid.print_grid()
game = Game()
game_update = pygame.USEREVENT #userevetn create an a custom veent
timer = pygame.time.set_timer(game_update, 500) # this will trigger the cusom event onvce evry 200 ms
while True:
    #.event.get() would make get all the evnt pygame recognise and put them in a list
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset_game()
            if event.key == pygame.K_s and game.game_over == False: 
                game.move_down()
                game.update_score(0,1)
            if event.key == pygame.K_a and game.game_over == False: 
                game.move_left()
            if event.key == pygame.K_w and game.game_over == False: 
                game.rotation()
            if event.key == pygame.K_d and game.game_over == False: 
                game.move_right()
        if event.type== game_update and game.game_over == False:
            game.move_down()

    score_value_surface = font.render(str(game.score), True, Colours.white)
    #.fill method would fill the display with colours, it accepts tuples, in a form of RGB
    display.fill(Colours.dark_blue)
    display.blit(score_surface, (365, 20, 50, 50))
    display.blit(next_surface, (375, 180, 50, 50))
    if game.game_over == True: display.blit(game_over_surface,(320,450,50,50))


    pygame.draw.rect(display, Colours.light_blue, score_rect)
    display.blit(score_value_surface, 
                score_value_surface.get_rect(centerx = score_rect.centerx, centery = score_rect.centery))
    pygame.draw.rect(display, Colours.light_blue, next_rect)
    game.draw_elements(display)
    pygame.display.update()
    clock.tick(frame)