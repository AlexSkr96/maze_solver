import unittest
from maze import Maze
from window import Window


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 12
        num_cols = 10
        window = win = Window(800, 600)
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, window)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )


if __name__ == "__main__":
    unittest.main()
