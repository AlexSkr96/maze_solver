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
        win,
        seed = None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        random.seed(seed)

        self._create_cells()


    def __repr__(self):
        res = ""
        for i in range(len(self._cells)):
            res += f"{i}: {self._cells[i]}\n"
        return res


    def _create_cells(self):
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                row.append(Cell(self._win))
            self._cells.append(row)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)

        self._break_entrance_and_exit()
        self._break_cells(0, 0)


    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + j * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)


    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0, 0)
        self._cells[-1][-1].bottom_wall = False
        self._draw_cell(self._num_rows-1, self._num_cols-1)


    def _break_cells(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            for modifier in (-1, 1):
                mod_i, mod_j = i + modifier, j + modifier
                if mod_i in range(self._num_rows) and not self._cells[mod_i][j].visited:
                    possible_directions.append((mod_i, j))

                if mod_j in range(self._num_cols) and not self._cells[i][mod_j].visited:
                    possible_directions.append((i, mod_j))

            if not possible_directions:
                return
            else:
                ind = possible_directions[random.randint(0, len(possible_directions)-1)]
                target_cell = self._cells[ind[0]][ind[1]]
                current_cell = self._cells[i][j]
                if ind[0] > i:
                    current_cell.bottom_wall = False
                    target_cell.top_wall = False
                elif ind[0] < i:
                    current_cell.top_wall = False
                    target_cell.bottom_wall = False
                elif ind[1] > j:
                    current_cell.right_wall = False
                    target_cell.left_wall = False
                elif ind[1] < j:
                    current_cell.left_wall = False
                    target_cell.right_wall = False

                self._draw_cell(i, j)
                self._draw_cell(ind[0], ind[1])
                self._break_cells(ind[0], ind[1])
