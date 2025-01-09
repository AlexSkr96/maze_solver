from line import Line
from point import Point
from cell import Cell
from window import Window


def main():
    win = Window(800, 600)

    # line1 = Line(
    #     Point(10, 10),
    #     Point(20, 20)
    # )
    # line2 = Line(
    #     Point(50, 10),
    #     Point(50, 150)
    # )
    # win.draw_line(line1, "red")
    # win.draw_line(line2)

    # cells = [
    #     Cell(200, 210, 200, 210, win),
    #     Cell(200, 210, 210, 220, win),
    #     Cell(200, 210, 220, 230, win),
    #     Cell(200, 210, 230, 240, win),
    #     Cell(210, 220, 220, 230, win),
    # ]
    # for i in range(3):
    #     cells[i].bottom_wall = False

    # for i in range(1, 4):
    #     cells[i].top_wall = False

    # cells[2].right_wall = False
    # cells[4].left_wall = False

    # for cell in cells:
    #     cell.draw()

    # cells[0].draw_move(cells[1])
    # cells[1].draw_move(cells[2])
    # cells[2].draw_move(cells[4])
    # cells[2].draw_move(cells[3], True)



    win.wait_for_close()


if __name__ == "__main__":
    main()
