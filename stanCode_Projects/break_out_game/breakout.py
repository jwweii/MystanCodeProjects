"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
This program will execute Bricks-Breaking game.
The players have three chances to break all the brisks.
The game will terminate if the ball is not caught by the paddle or all the bricks are broken.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 4000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    dx = graphics.dx  # get the x-axis velocity.
    dy = graphics.dy  # get the y-axis velocity.
    lives = NUM_LIVES
    brick_num = graphics.brick_num  # get the number of bricks.
    # Add animation loop here!
    while True:
        if graphics.click_n == 0:  # keep game off
            pause(FRAME_RATE)
        if graphics.click_n >= 1:
            graphics.ball.move(dx, dy)  # start the game after mouse click.
            # change x-axis direction if hit wall
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                dx = -dx
            # change y-axis direction if hit paddle.
            if graphics.ball.y <= 0 or graphics.ball_in_object() == 'paddle':
                dy = -dy
                if graphics.ball.y > graphics.paddle.y+1:
                    dy = graphics.dy
            # loss life or reset ball if hit the bottom.
            if graphics.ball.y >= graphics.window.height:
                lives -= 1
                if lives == 0:
                    break
                else:
                    graphics.reset_ball()
            # change direction and remove bricks if hit brick
            if graphics.ball_in_object() == 'bricks':
                dy = -dy
                brick_num -= 1
                impact_object = graphics.object
                graphics.window.remove(impact_object)
                if brick_num == 0:
                    break
            pause(FRAME_RATE)


if __name__ == '__main__':
    main()
