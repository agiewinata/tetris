from grid import Grids
from all_blocks import *
from block_parent import *
import random

class Game:

    #initialise everything
    def __init__(self):
        self.grid = Grids()
        #put every tetrominos into a list.
        self.block_list = [IBlock(), L_Block(), JBlock(), SBlock(), OBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0

    """
    This method is responsible for returning a random tetrominos
    to display on the scree. once chosen, the block would be removed
    from its list to prevent redundacy. The list itself would bre refreshed 
    after its length is 0.
    """
    def get_random_block(self):
        if len(self.block_list) == 0:
            self.block_list = [IBlock(), L_Block(), JBlock(), SBlock(), OBlock(), TBlock(), ZBlock()]
        random_block = random.choice(self.block_list)
        self.block_list.remove(random_block)
        return random_block

    """
    This method would check if the tetromino is inside of the grid or not
    it uses the .find_cell.position() to find the position of the blocks, 
    which then is checked by the .is_inside method. It returns a boolean.
    """
    def block_inside(self):
        cell_positions = self.current_block.find_cell_position()
        for cell in cell_positions:
            if self.grid.is_inside(cell.rows, cell.columns) == False:
                return False
        else:
            return True
        
    """
    This method is responsible for many of the game logic.
    it would lock the current block within the gird. 
    assign the current_block with next_blcok, while initialising
    the next next_block element. clear full rows, Update the score, 
    and check for a game over.
    """
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
            pygame.event.clear()

    """
    check if the current tetromino is collideing with existing 
    tetrominos in the board. it uses the .find_cell_position
    to first fin out the exact coordinate of the tetrominos
    and then check if it fits by the .is_empty method.
    This method would return a boolean vallue
    """
    def check_block_fits(self):
        tiles = self.current_block.find_cell_position()
        for position in tiles:
            if self.grid.is_empty(position.rows, position.columns)==False:  
                    return False 
        return True
    
    """
    This method would reset all the necessary variable apon a game over.
    """
    def reset_game(self):
        self.grid.reset_grid()
        self.blocks = [IBlock(), L_Block(), JBlock(), SBlock(), OBlock(), TBlock(), ZBlock()]
        self.current_block=self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    """
    all the move method, would move the tetrominos with the .move method. 
    Before moving it woould check wheter the bolck is inside of the grid and
    colliding with any other blocks. if this condition is not fulffilled, it would
    undo and movement.
    """
    def move_down(self): 
        self.current_block.move(1,0)
        if self.block_inside() == False or self.check_block_fits() == False:
            self.current_block.move(-1,0)
            self.lock_block() #to make sure that the bottom block does not leave the grid

    def move_left(self): 
        self.current_block.move(0,-1)
        if self.block_inside() == False or self.check_block_fits() == False:
            self.current_block.move(0,1)

    def move_right(self): 
        self.current_block.move(0,1)
        if self.block_inside() == False or self.check_block_fits() == False:
            self.current_block.move(0,-1)

    """
    would ratate the element based on certain condition. if these conditions
    werent met it would undo the rotation.
    """
    def rotation(self):
        self.current_block.block_rotation()
        if self.block_inside() == False or self.check_block_fits() == False:
            self.current_block.undo_rotation()
    
    """
    Would draw the current and next tetromino on a specific part of the screen
    some tetrominos assigned to next_block have different offset due to their 
    dimensions.
    """
    def draw_elements(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen,255,290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)

    """
    The game scoring system, the score would be updated propotionaly
    to how many the lines are cleared and whether the user moved the 
    tetrominos down by themselved. 
    """
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points
    


