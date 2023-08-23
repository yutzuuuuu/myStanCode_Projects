"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This is Bricks Breakout Game, you have three lives,
try it and see how many scores you can get!!!
Let's start~
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10   # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    while True:
        pause(FRAME_RATE)
        if graphics.bricks_amount == graphics.score:
            break
        if lives == 0:
            graphics.is_playing = False
            graphics.lose()
            break
        if graphics.is_playing:
            if lives > 0:
                vx = graphics.get_dx()
                vy = graphics.get_dy()
                while True:
                    graphics.ball.move(vx, vy)
                    maybe_obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                    maybe_obj2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
                    maybe_obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.width)
                    maybe_obj4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y + graphics.ball.width)
                    if maybe_obj1 is not None and maybe_obj1 is not graphics.score_label:
                        if maybe_obj1 is graphics.paddle:
                            if vy > 0:  # when ball fall vy > 0
                                vy = -vy
                        else:
                            vy = -vy
                            graphics.window.remove(maybe_obj1)
                            graphics.score += 1
                            graphics.score_label.text = 'Score=' + str(graphics.score)
                    elif maybe_obj2 is not None and maybe_obj2 is not graphics.score_label:
                        if maybe_obj2 is graphics.paddle:
                            if vy > 0:
                                vy = -vy
                        else:
                            vy = -vy
                            graphics.window.remove(maybe_obj2)
                            graphics.score += 1
                            graphics.score_label.text = 'Score=' + str(graphics.score)
                    elif maybe_obj3 is not None and maybe_obj3 is not graphics.score_label:
                        if maybe_obj3 is graphics.paddle:
                            if vy > 0:
                                vy = -vy
                        else:
                            vy = -vy
                            graphics.window.remove(maybe_obj3)
                            graphics.score += 1
                            graphics.score_label.text = 'Score=' + str(graphics.score)
                    elif maybe_obj4 is not None and maybe_obj4 is not graphics.score_label:
                        if maybe_obj4 is graphics.paddle:
                            if vy > 0:
                                vy = -vy
                        else:
                            vy = -vy
                            graphics.window.remove(maybe_obj4)
                            graphics.score += 1
                            graphics.score_label.text = 'Score=' + str(graphics.score)
                    elif graphics.bricks_amount == graphics.score:
                        graphics.is_playing = False
                        graphics.win()
                        break
                    elif graphics.ball.x <= 0:
                        if vx < 0:
                            vx = -vx
                    elif graphics.ball.x + graphics.ball.width >= graphics.window.width:
                        if vx > 0:
                            vx = -vx
                    elif graphics.ball.y <= 0:
                        vy = -vy
                    elif graphics.ball.y - graphics.ball.width >= graphics.window.height:
                        lives -= 1
                        graphics.reset_ball()
                        graphics.is_playing = False
                        if lives == 2:
                            graphics.window.remove(graphics.heart1)
                        elif lives == 1:
                            graphics.window.remove(graphics.heart2)
                        else:
                            graphics.window.remove(graphics.heart3)
                        break
                    pause(FRAME_RATE)


if __name__ == '__main__':
    main()
