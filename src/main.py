from window import Window
from maze import Maze


def main():
    num_rows = 10
    num_cols = 8
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = 50
    cell_size_y = 50
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
