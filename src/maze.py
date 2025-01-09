from cell import Cell


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
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()


    def _create_cells(self):
        x = self.x1
        y = self.y1
        for _ in range(self.num_rows):
            self._cells.append([])
            cells_row = self._cells[-1]
            for _ in range(self.num_cols):
                cells_row.append(
                    Cell(x, y, x + self.cell_size_x, y + self.cell_size_y, self.win)
                )
                x += self.cell_size_x

            y += self.cell_size_y


    def _animate(self):
        self.win.redraw()
        time.sleep(1/60)
