"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    new_line = []
    merge_line = []
    merged = False
    indx2 = 0

    for indx1 in range(len(line)):
        new_line.append(0)
        
    for indx1 in range(len(line)):
        if (line[indx1] != 0):
            new_line[indx2] = line[indx1]
            indx2 += 1

    for indx1 in range(len(line) - 1):
        if(new_line[indx1] != 0):
            if ((new_line[indx1] == new_line[indx1+1]) and (merged == False)):
                merge_line.append(2*new_line[indx1])
                merged = True
            elif ((new_line[indx1] != new_line[indx1+1]) and (merged == False)):     
                merge_line.append(new_line[indx1])
            elif (merged == True):
                merged = False
        else:
            merged = True

    if ((new_line[-1] != 0) and (merged == False)):
        merge_line.append(new_line[-1]) 
    
    while (len(merge_line) < len(line)):
        merge_line.append(0)

    return merge_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._grid = []
        self.reset()
        
        # The following is a dictionary of initial tiles
        # to be used in the move function
        self._initial_tiles = {UP: [[0,index] for index in range(self.get_grid_width())],
                              DOWN: [[self.get_grid_height() - 1,index] for index in range(self.get_grid_width())],
                              LEFT: [[index, 0] for index in range(self.get_grid_height())],
                              RIGHT: [[index, self.get_grid_width() - 1] for index in range(self.get_grid_height())]}


    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._grid = [[0 for dummy_col in range(self._grid_width)]
                           for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        initial_list = self._initial_tiles[direction]
        temp_list = []
        
        # The following function executes the steps described in Phase Three of the project description
        def row_merge(self, initial_list, direction, temp_list, row_index):
            """
            Merges the row in the conditional statement that follows.
            If the row is merged a new tile is added.
            """
            pre_move_grid = str(self._grid)
            
            for init in initial_list:
                temp_list.append(init)
                for dummy_index in range(1, row_index):
                    temp_list.append([x + y for x,y in zip(temp_list[-1], OFFSETS[direction])])
                    line = []
                    for pair in temp_list:
                        line.append(self.get_tile(pair[0],pair[1]))
                        
                merged_line = merge(line)
                
                for index, pair in zip(merged_line, temp_list):
                    self.set_tile(pair[0], pair[1], index)
                    
                temp_list = []
                
            post_move_grid = str(self._grid)
            
            if post_move_grid != pre_move_grid:
                self.new_tile()
                
        # Apply the above function to complete the move.
        if ((direction == UP) or (direction == DOWN)):
            row_merge(self, initial_list, direction, temp_list, self.get_grid_height())
        elif ((direction == LEFT) or (direction == RIGHT)):
            row_merge(self, initial_list, direction, temp_list, self.get_grid_width())            

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # Create a list of open positions in the grid - i.e. grid positions whose value is 0.
        # If there are no such positions, then the game is over.
        # Otherwise, pick an open position at random and fill it with a randomly
        # chosen tile from tile_list.
        open_pos = []
        for row in range(self._grid_height):
            for col in range(self._grid_width):
                if (self._grid[row][col] == 0):
                    open_pos.append([row,col])
        if (open_pos == []):
            print "Game Over"
        else:
            tile_pos = random.choice(open_pos)
            
        tile_list = []
        for dummy_index in range(90):
            tile_list.append(2)
        for dummy_index in range(10):
            tile_list.append(4)
            
        tile = random.choice(tile_list)
        self.set_tile(tile_pos[0],tile_pos[1],tile)
        

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
