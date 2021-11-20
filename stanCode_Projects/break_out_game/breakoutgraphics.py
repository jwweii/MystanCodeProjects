"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
This program provide the constructors needed for the game – bricks breaking.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:
    """
    The class will prepare the bricks, ball, and paddle on the canvas for the game.
    By mouse listeners, players are able to control the paddle and start the game by a mouse click.
    The program can detect objects collided by the ball.
    """

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self. window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window_width-PADDLE_WIDTH)/2, self.window_height-paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius, ball_radius)
        self.ball.filled = True
        self.window.add(self.ball, (self.window_width-ball_radius)/2, (self.window_height-ball_radius)/2)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Initialize our mouse listeners
        self.click_n = 0  # the number of mouse clicks.
        self.__maybe_object = None  # default setting of object impacted by the ball.
        onmouseclicked(self.game_start)
        onmousemoved(self.paddle_move)

        # Draw bricks
        self.__brick_num = brick_rows * brick_cols  # the number of bricks
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.__brick = GRect(brick_width, brick_height, x=0 + j*(brick_width + brick_spacing),
                                     y=brick_offset + i*(brick_height + brick_spacing))
                if i/brick_rows < 0.2:
                    self.__color = 'red'
                elif 0.2 <= i/brick_rows < 0.4:
                    self.__color = 'orange'
                elif 0.4 <= i/brick_rows < 0.6:
                    self.__color = 'yellow'
                elif 0.6 <= i/brick_rows < 0.8:
                    self.__color = 'green'
                else:
                    self.__color = 'blue'
                self.__brick.color = self.__color
                self.__brick.filled = True
                self.__brick.fill_color = self.__color
                self.window.add(self.__brick)

    @property
    def dx(self):  # velocity of x-axis
        return self.__dx

    @property
    def dy(self):  # velocity of y-axis
        return self.__dy

    @property
    def brick_num(self):
        return self.__brick_num

    def paddle_move(self, mouse, paddle_offset=PADDLE_OFFSET, paddle_width=PADDLE_WIDTH):
        """
        The function will allow player to control the paddle withing the canvas.
        """
        mid_paddle = mouse.x - paddle_width / 2
        if mouse.x < paddle_width:
            mid_paddle = 0
        elif mouse.x > self.window_width - paddle_width:
            mid_paddle = self.window_width - paddle_width
        self.window.add(self.paddle, mid_paddle, self.window_height-paddle_offset)

    def game_start(self, mouse):
        """
        by clicking the mouse, the function will add numbers of clicks and this variable will be the switch of the game.
        """
        self.click_n += 1

    def ball_in_object(self, ball_radius=BALL_RADIUS):
        """
        This function will detect whether the ball hit objects or not.
        """
        collision = 'none'
        ball_x = self.ball.x
        ball_y = self.ball.y
        for i in range(0, 2, 2):  # to check four corners of the ball.
            for j in range(0, 2, 2):
                self.__maybe_object = self.window.get_object_at(ball_x+i*ball_radius, ball_y+j*ball_radius)
                if self.__maybe_object is not None:
                    collision = 'bricks'
                if self.__maybe_object == self.paddle:
                    collision = 'paddle'
        return collision

    @property
    def object(self):
        return self.__maybe_object

    def reset_ball(self, ball_radius=BALL_RADIUS):
        self.window.add(self.ball, (self.window_width - ball_radius) / 2, (self.window_height - ball_radius) / 2)