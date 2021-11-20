"""
File: sierpinski.py
Name: 
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO: The program will draw Sierpinski triangles.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: the levels of the picture.
	:param length: the triangle's length
	:param upper_left_x: the point of x-axis at the upper point
	:param upper_left_y: the point of y-axis at the upper point
	"""
	if order == 0:
		pass
	else:
		add_triangle(length, upper_left_x, upper_left_y)
		length /= 2
		order -= 1
		sierpinski_triangle(order, length, upper_left_x, upper_left_y)
		sierpinski_triangle(order, length, upper_left_x + length, upper_left_y)
		sierpinski_triangle(order, length, upper_left_x + length / 2, upper_left_y + length * 0.886)


def add_triangle(length, upper_left_x, upper_left_y):
	"""
	The function will draw a triangle.
	"""
	middle_x = upper_left_x + length / 2
	middle_y = upper_left_y + length * 0.886
	upper_right_x = upper_left_x + length
	upper_right_y = upper_left_y
	left_line = GLine(upper_left_x, upper_left_y, middle_x, middle_y)
	upper_line = GLine(upper_left_x, upper_left_y, upper_right_x, upper_right_y)
	right_line = GLine(upper_right_x, upper_right_y, middle_x, middle_y)
	window.add(left_line)
	window.add(upper_line)
	window.add(right_line)


if __name__ == '__main__':
	main()