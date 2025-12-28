import pygame
from colours import Colours
import sys

class Grids:
    # initialise all the value needed for the grid
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        #creates a 2d array to make the map
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colour = Colours.get_all_colours()

    #method for debugging
    def print_grid(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                print(self.grid[row][col], end = ' ')
            print()
    
    """
    A method to check whether the tetrominos are inside of the grid or now.
    It returns a boolean value.
    """
    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        else:
            return False

    """
    A method that checks wether the grid is empty or not. it is used in
    collision detection, and it returns a boolean value.
    """
    def is_empty(self, row, column):
        if self.grid[row][column]==0:
            return True
        else:
            return False
    
    """
    A method that checks whether a row inside of the gird is full.
    This emthod i used for the scoring feature of this game.
    It return a boolean.
    """
    def is_row_full(self,row):
        for column in range(self.num_cols):
            if self.grid[row][column]==0:
                return False
        return True
    
    """
    A method that would clear the rows when called.
    This method is used in the scoring section of the game.
    """
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column]=0

    """
    A method that would move down existing block on the grid.
    It is used as a part of the scoring section of this game.
    """
    def move_row_down(self,row,num_rows):
        for column in range(self.num_cols):
            self.grid[row+num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    """
    This method is reponsible for the complete logic of the clearing
    rows logic for the game. It firste check wheter a row is full or 
    not. if it is, The method would clear the row, and move down the 
    existing blocks according to the number that is assigned to completed.   
    """
    def clear_full_rows(self):
        completed = 0
        for row in range (self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed >= 1:
                self.move_row_down(row, completed)
        return completed

    """
    This method is used for resetting the board upon a game over.
    """
    def reset_grid(self):
        for row in range(self.num_rows):
            for col in range (self.num_cols):
                self.grid[row][col] = 0

    """
    This method is responsible for drawing the actual grid. first
    the cell value is get, and both x and y coordinates are calculated. 
    Afterward the sides of the tiles is calculated so that we may get the
    sise of teh tiles.
    """
    def draw(self, display):
        for row in range(self.num_rows):
            for cols in range (self.num_cols):
                cell_value = self.grid[row][cols]
                x_coordinate = cols * self.cell_size + 11
                y_coordinate = row * self.cell_size + 11
                side = self.cell_size - 1
                cell_rectangle = pygame.Rect(x_coordinate, y_coordinate, side, side)
                pygame.draw.rect(display, self.colour[cell_value], cell_rectangle)



