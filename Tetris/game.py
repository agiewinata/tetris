from grid import Grids
from all_blocks import *
from block_parent import *
import random

class Game:

    def __init__(self):
        self.grid = Grids()
        self.block_list = [ IBlock(), L_Block(), JBlock(), SBlock(), OBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

    def get_random_block(self):
        if len(self.block_list) == 0:
            self.block_list = [IBlock(), L_Block(), JBlock(), SBlock(), OBlock(), TBlock(), ZBlock()]
        random_block = random.choice(self.block_list)
        self.block_list.remove(random_block)
        return random_block

    def block_inside(self):
        cell_positions = self.current_block.find_cell_position()
        for cell in cell_positions:
            if self.grid.is_inside(cell.rows, cell.columns) == False:
                return False
        else:
            return True
        
    def lock_block(self):
        tiles = self.current_block.find_cell_position()
        for position in tiles:
            self.grid.grid[position.rows][position.columns] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()
        self.update_score(rows_cleared,0)
        if self.check_block_fits()==False:
            self.game_over = True


    def check_block_fits(self):
        tiles = self.current_block.find_cell_position()
        for position in tiles:
            if self.grid.is_empty(position.rows, position.columns)==False:  
                return False
        return True

    def reset_game(self):
        self.grid.reset_grid()
        self.blocks = [IBlock(), L_Block(), JBlock(), SBlock(), OBlock(), TBlock(), ZBlock()]
        self.current_block=self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def move_down(self): 
        self.current_block.move(1,0)
        if self.block_inside() == False or self.check_block_fits() == False:
            self.current_block.move(-1,0)
            self.lock_block()
    def move_left(self): 
        self.current_block.move(0,-1)
        if self.block_inside() == False or self.check_block_fits() == False:
            self.current_block.move(0,1)
    def move_right(self): 
        self.current_block.move(0,1)
        if self.block_inside() == False or self.check_block_fits() == False:
            self.current_block.move(0,-1)
    """
        def move_up(self): 
        self.current_block.move(-1,0)
        if self.block_inside() == False:
            self.current_block.move(1,0)
    """

    def rotation(self):
        self.current_block.block_rotation()
        if self.block_inside() == False or self.check_block_fits() == False:
            self.current_block.undo_rotation()
    
    def draw_elements(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)
        
        if self.next_block.id == 3:
            self.next_block.draw(screen,255,290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points
    


