import pygame
from colours import Colours
from position import Position

class Block:
    #initialising everything
    def __init__(self, id):
        self.id = id
        self.cells_position = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colours = Colours.get_all_colours()

    # move the box by a certain rows and columns
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    """
    block ration rotate the block based on a predetrmined coordinate
    in all_blocks.py. it would reset once the tetrominos has 
    been rotated through all possible rotation, so that user
    can rotate it once more.
    """
    def block_rotation(self):
        self.rotation_state +=1
        if self.rotation_state == len(self.cells_position):
            self.rotation_state = 0

    """
    this method is responsible for undoing a rotation, it would
    decrease the rotation_state,a s to not use up a rotation
    """
    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state < 0:
            self.rotation_state = len(self.cells_position) - 1
    
    """
    This method is responsible for finding the position of the 
    tetrominos. it returns a list of Position class element of 
    where the tetrominos is.
    """
    def find_cell_position(self):
        moved_cells = []
        cells = self.cells_position[self.rotation_state]
        for cell in cells:
            y_movement = cell.columns + self.column_offset
            x_movement = cell.rows + self.row_offset
            position = Position(x_movement, y_movement)
            moved_cells.append(position)
        return moved_cells

    """
    This method is responsible for draing the tetrominos
    according to the list given by the .find_cell_position
    method and its offset. The offset is responsible for drawing
    the tetriminos is specific part of the display, while the 
    actual position of the tetrominos is contained within the 
    list from .find_cell_position
    """
    def draw(self, display, offsetx, offsety):
        tetrominos = self.find_cell_position()
        for tetromino in tetrominos:
            y_position = tetromino.rows * self.cell_size + offsety
            x_position = tetromino.columns * self.cell_size + offsetx
            side_length = self.cell_size - 1
            colours = self.colours[self.id]

            tetromino_rect = pygame.Rect(x_position, y_position, side_length, side_length)
            pygame.draw.rect(display, colours, tetromino_rect )

