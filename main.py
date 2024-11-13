from graphics import Window
from cell import Cell


def main():
    win = Window(800, 600)

    c = Cell(win)
    c.draw(50, 50, 100, 100)

    c2 = Cell(win)
    c2.draw(125, 125, 200, 200)

    c.draw_move(c2)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225, 225, 250, 250)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)

    win.wait_for_close()


main()
