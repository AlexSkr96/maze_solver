from line import Line
from point import Point
from window import Window


def main():
    win = Window(800, 600)
    line1 = Line(
        Point(10, 10),
        Point(20, 20)
    )
    line2 = Line(
        Point(50, 10),
        Point(50, 150)
    )
    win.draw_line(line1, "red")
    win.draw_line(line2, "black")
    win.wait_for_close()


if __name__ == "__main__":
    main()
