"""
File: draw line
Name: Chien-Wei Peng
-------------------------
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10

window = GWindow()
point = GOval(SIZE, SIZE)
count = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)
    point.filled = True


def draw_line(mouse):
    """
    The function will draw a circle at an odd number of click and a line at an even number click.
    """
    global count
    count += 1  # the sum of click number.
    if count % 2 == 1:  # to decide each click is an odd or even number.
        window.add(point, mouse.x - SIZE / 2, mouse.y - SIZE / 2)
    else:
        line = GLine(point.x, point.y, mouse.x, mouse.y)
        window.add(line)
        window.remove(point)


if __name__ == "__main__":
    main()
