"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.graphics.gimage import GImage
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball
FRAME_RATE = 10


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(width=paddle_width, height=paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width/2-self.paddle.width/2),
                        y=self.window.height-paddle_offset-paddle_height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2, x=self.window.width/2-ball_radius, y=self.window.height/2-ball_radius)
        self.ball.filled = True
        self.window.add(self.ball)

        # create score label
        self.score = 0
        self.score_label = GLabel('Score= ' + str(self.score))
        self.score_label.font = 'Courier-40-bold'
        self .window.add(self.score_label, x=0, y=self.score_label.height+15)

        # lives count img
        self.heart1 = GImage('heart.png')
        self.window.add(self.heart1, x=300, y=10)
        self.heart2 = GImage('heart.png')
        self.window.add(self.heart2, x=340, y=10)
        self.heart3 = GImage('heart.png')
        self.window.add(self.heart3, x=380, y=10)

        # control game
        self.is_playing = False

        # Draw bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.bricks = GRect(width=brick_width, height=brick_height, x=(brick_width + brick_spacing) * j,
                                    y=brick_offset + (brick_height + brick_spacing) * i)
                self.bricks.filled = True
                self.window.add(self.bricks)
                a = brick_cols / 5  # 5=how many color
                if i < a:
                    self.bricks.fill_color = 'maroon'
                elif i < a * 2:
                    self.bricks.fill_color = 'indianred'
                elif i < a * 3:
                    self.bricks.fill_color = 'lightcoral'
                elif i < a * 4:
                    self.bricks.fill_color = 'rosybrown'
                else:
                    self.bricks.fill_color = 'mistyrose'
        self.bricks_amount = brick_cols * brick_rows

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.handle_click)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

    def paddle_move(self, mouse):
        if mouse.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif mouse.x >= self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width/2

    def handle_click(self, event):
        self.is_playing = True

    def reset_ball(self):
        self.ball.x = self.window.width/2-BALL_RADIUS
        self.ball.y = self.window.height/2-BALL_RADIUS

    def win(self):
        cong_label = GLabel('You Win !')
        cong_label.font = 'Courier-40-italic-bold'
        self.window.add(cong_label, x=self.window.width/4, y=self.window.height/2)

    def lose(self):
        lose_label = GLabel('Gameover')
        lose_label.font = 'Courier-60-italic-bold'
        self.window.add(lose_label, x=self.window.width/6, y=self.window.height / 2)

    def get_dx(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        return self.__dx

    def get_dy(self):
        return INITIAL_Y_SPEED

    def get_radius(self):
        return BALL_RADIUS
