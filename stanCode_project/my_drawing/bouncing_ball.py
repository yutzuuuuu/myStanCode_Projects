"""
File: bouncing_ball.py
Name: Jessie
-------------------------
This program can simulates ball bouncing.
And once the ball over the scree three times,
it will be stop.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
times = 0  # times the ball out of screen
is_clicked = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(bouncing)
    global is_clicked, times, GRAVITY
    while True:
        if is_clicked:
            if times < 3:
                vy = 0
                while True:
                    ball.move(VX, vy)
                    vy += GRAVITY
                    if (ball.y + ball.height) >= window.height and vy > 0:
                        vy = -vy * REDUCE
                    elif (ball.x + ball.width) >= window.width:
                        times += 1
                        ball.x = START_X
                        ball.y = START_Y
                        is_clicked = False
                        break
                    pause(DELAY)
            else:
                break
        pause(DELAY)


def bouncing(click):
    global is_clicked
    is_clicked = True



if __name__ == "__main__":
    main()
