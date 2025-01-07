from point import Point
from line import Line
from window import Window


class Cell:
    def __init__(self, x1, x2, y1, y2, win):
        self.top_wall = True
        self.bottom_wall = True
        self.left_wall = True
        self.right_wall = True
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__win = win


    def draw(self):
        if self.top_wall:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            )

        if self.bottom_wall:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            )

        if self.left_wall:
            self.__win.draw_line(
                Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            )

        if self.right_wall:
            self.__win.draw_line(
                Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            )
