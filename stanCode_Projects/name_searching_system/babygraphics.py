"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    margin = GRAPH_MARGIN_SIZE
    x = margin + year_index * ((width - 2 * margin) / len(YEARS))
    return x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    margin = GRAPH_MARGIN_SIZE
    canvas.create_line(margin, margin, CANVAS_WIDTH - margin, margin)
    canvas.create_line(margin, CANVAS_HEIGHT - margin, CANVAS_WIDTH - margin, CANVAS_HEIGHT - margin)
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, margin, x, CANVAS_HEIGHT)
        canvas.create_text(x, CANVAS_HEIGHT - margin, anchor=tkinter.NW, text=YEARS[i])


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    # make the color of line be rotated in four colors. the default is -1, so the number in the first round will be 0.
    color_turn = -1
    y_length = CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE  # the length of each line
    for name in lookup_names:
        color_turn += 1
        for i in range(int(YEARS[0]), int(YEARS[11]) + 10, 10):
            x1 = GRAPH_MARGIN_SIZE + ((i - 1900) / 10) * 80
            year = str(i)
            if year in name_data[name]:
                rank = name_data[name][year]
                y1 = GRAPH_MARGIN_SIZE + y_length * (int(rank) / 1000)
                canvas.create_text(x1 + TEXT_DX, y1, anchor=tkinter.NW, text=name + rank, fill=COLORS[color_turn % 4])
            # if the rank is out of 1000, * will be showed.
            else:
                rank = '*'
                y1 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                canvas.create_text(x1 + TEXT_DX, y1, anchor=tkinter.NW, text=name + rank, fill=COLORS[color_turn % 4])
            # to get the second x and y of a line, we need to know the rank in the next decade.
            next_decade = str(int(year) + 10)
            if int(next_decade) <= 2010:
                x2 = x1 + 80
                if next_decade in name_data[name]:
                    rank_next = name_data[name][next_decade]
                    y2 = GRAPH_MARGIN_SIZE + y_length * (int(rank_next) / 1000)
                else:
                    y2 = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                canvas.create_line(x1, y1, x2, y2, fill=COLORS[color_turn % 4])


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
