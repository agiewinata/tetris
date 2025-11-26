import pygame
from colours import Colours
from position import Position

class Block:
    def __init__(self, id):
        self.id = id
        self.cells_position = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colours = Colours.get_all_colours()

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    def block_rotation(self):
        self.rotation_state +=1
        if self.rotation_state == len(self.cells_position):
            self.rotation_state = 0

    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells_position)- 1
    
    def find_cell_position(self):
        moved_cells = []
        cells = self.cells_position[self.rotation_state]
        for cell in cells:
            y_movement = cell.columns + self.column_offset
            x_movement = cell.rows + self.row_offset
            position = Position(x_movement, y_movement)
            moved_cells.append(position)
        return moved_cells

    def draw(self, display, offsetx, offsety):
        tetrominos = self.find_cell_position()
        for tetromino in tetrominos:
            y_position = tetromino.rows * self.cell_size + offsety
            x_position = tetromino.columns * self.cell_size + offsetx
            side_length = self.cell_size-1
            colours = self.colours[self.id]

            tetromino_rect = pygame.Rect(x_position, y_position, side_length, side_length)
            pygame.draw.rect(display, colours, tetromino_rect )

