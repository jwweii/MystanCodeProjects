"""
File: bouncing_ball
Name: Chien-Wei Peng
-------------------------
TODO: This program will simulate a bouncing ball after click mouse three times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 2.5
DELAY = 30
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
switch_n = 0
round_n = 0


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(switch)
    ball.filled = True
    window.add(ball, START_X, START_Y)


def bouncing_ball():
    """
    This is the function to simulate a bouncing ball.
    """
    global switch_n, round_n
    vx = VX
    gx = 1
    while True:
        ball.move(vx, gx)
        if ball.x + ball.width >= window.width:  # return to default setting if the ball is out of the canvas.
            window.add(ball, START_X, START_Y)
            switch_n = 0  # return to default setting and wait for mouse click.
            round_n += 1  # after round 3 the mouse click will not activate the stimulation.
            window.remove(ball)
            break
        if ball.y + ball.height >= window.height:
            gx = -(gx * REDUCE)
            if ball.y + ball.height >= window.height and gx > 0:  # prevent the ball falling out of the canvas.
                gx = -gx
        pause(DELAY)
        gx += GRAVITY
        if ball.y + ball.height >= window.height and gx > 0:
            gx = 0  # prevent the ball falling out of the canvas.
    window.add(ball, START_X, START_Y)


def switch(mouse):
    """
    This function will control the start of the simulation.
    When click mouse once, the switch_n will add 1. the function will be activated only when switch_n = 1.
    """
    global switch_n, round_n
    switch_n += 1
    if round_n == 3:
        switch_n = 99  # after round 3 the function will not be activated again.
    if switch_n == 1:
        bouncing_ball()


if __name__ == "__main__":
    main()
