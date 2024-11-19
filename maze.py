from cell import Cell 
import random
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        animateBool=False,
        seed=None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._animateBool = animateBool
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(col, row)
    
    def _draw_cell(self, col, row):
        if self._win is None:
            return
        x1 = self._x1 + col * self._cell_size_x
        y1 = self._y1 + row * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[col][row].draw(x1, y1, x2, y2)
        if self._animateBool == True:
            self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_right_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
    def _break_walls_r(self, col, row):
        self._cells[col][row].visited = True
        running = True
        while running:
            to_visit_directions = []
            #left
            if col > 0 and not self._cells[col - 1][row].visited:
                to_visit_directions.append((col - 1, row))
            #right
            if col < self._num_cols - 1 and not self._cells[col + 1][row].visited:
                to_visit_directions.append((col + 1, row))
            #up
            if row > 0 and not self._cells[col][row - 1].visited:
                to_visit_directions.append((col, row - 1))
            #down
            if row < self._num_rows - 1 and not self._cells[col][row + 1].visited:
                to_visit_directions.append((col, row + 1))
            if len(to_visit_directions) == 0:
                self._draw_cell(col, row)
                return
            
            random.shuffle(to_visit_directions)
            next_direction = to_visit_directions.pop()

            if next_direction[0] == col - 1:
                self._cells[col][row].has_left_wall = False
                self._cells[col - 1][row].has_right_wall = False
            if next_direction[0] == col + 1:
                self._cells[col][row].has_right_wall = False
                self._cells[col + 1][row].has_left_wall = False
            if next_direction[1] == row - 1:
                self._cells[col][row].has_top_wall = False
                self._cells[col][row - 1].has_bottom_wall = False
            if next_direction[1] == row + 1:
                self._cells[col][row].has_bottom_wall = False
                self._cells[col][row + 1].has_top_wall = False
            
            self._break_walls_r(next_direction[0], next_direction[1])


    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
