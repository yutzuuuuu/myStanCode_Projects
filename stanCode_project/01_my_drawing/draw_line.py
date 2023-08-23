"""
File: draw_line.py
Name: Jessie
-------------------------
This program can draw a line when user
clicking on GWindow
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


# This constant controls the size of the circle
SIZE = 20


# Global Variable
window = GWindow()
circle = GOval(SIZE, SIZE)
click = 1


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)  # draw circle or line


def draw(mouse):
    global click
    # if click is odd draw a hollow circle
    if click % 2 == 1:
        circle.filled = True
        circle.fill_color = 'white'
        window.add(circle, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        click += 1
    # if click is even draw a line
    else:
        line = GLine(x0=circle.x+SIZE/2, y0=circle.y+SIZE/2, x1=mouse.x, y1=mouse.y)
        window.add(line)
        window.remove(circle)
        click += 1


if __name__ == "__main__":
    main()
