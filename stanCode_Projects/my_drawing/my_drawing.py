"""
File: Human chromosomes generator
Name: Chien-Wei Peng
----------------------
TODO: This program will automatically draw picture of 23-pairs human chromosomes.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow
import random as r


SIZE = 10


window = GWindow(1250, 820)


def main():
    """
    TODO: The main function will draw human chromosomes by following steps:
    1. decide the sex
    2. draw 22-pairs of somatic chromosomes
    3. draw sex chromosomes as XX or XY according to the sex.
    4. add title
    """
    n = 0  # the parameter of the position of each pair of chromosome
    pair_n = 0  # the parameter of the position of the 2nd chromosome in each pair of chromosome
    sex = r.choice('MF')  # decide the sex randomly; M: male; F: female
    chromosome(n, pair_n)
    sex_chromosome(sex)
    title(sex)


def chromosome(n, pair_n):
    """
    This is the function for somatic chromosome drawing.
    The function will leverage four loops to decide the location and length of each chromosomes in the picture.
    The length of each chromosomes will simulate the nature chromosomes, from the longest to the shortest.
    The chromosomes will randomly deviate to left or right as nature condition.
    """
    for i in range(1, 5):  # This loop will draw the first to forth line of chromosomes in the picture
        y_axis = y_start(i)
        x_start = 100
        x_end = 1201
        if i == 4:  # set the end of somatic chromosome on the forth line. (The following will be sex chromosomes.)
            x_end = 800
        for j in range(x_start, x_end, 200):  # This loop will decide the position of each chromosomes.
            x_axis = j
            x2_axis = j + 50
            n += (j//100) * 2
            pair_n += 1
            chromosome_length = y_axis + 150 - n
            if i != 1:
                chromosome_length = y_axis + 150 - n//2  # to gradually shorten the length of each chromosome as nature
            for k in range(y_axis, chromosome_length):
                x_variation = r.choice(range(-3, 4))  # to generate of the effect of nature deviation to left or right
                x2_variation = r.choice(range(-3, 4))
                x_axis += x_variation
                x2_axis += x2_variation
                chromosome1 = GOval(SIZE, SIZE, x=x_axis, y=k)
                chromosome1.color = 'darkgray'
                chromosome2 = GOval(SIZE, SIZE, x=x2_axis, y=k)
                chromosome2.color = 'darkgray'
                chromosome_density = r.choice(range(10)) # to generate the effect of different densities
                if chromosome_density < 8:
                    window.add(chromosome1)
                    window.add(chromosome2)
            label = label_n(i, pair_n, j, y_axis)
            label.font = '-16'
            window.add(label)


def sex_chromosome(sex):
    """
    This function will draw sex chromosomes.
    If the sex is male, it will draw XY.
    If the sex is female, it will draw XX.
    """
    y_axis1 = 580
    x_axis1 = 920
    x_axis2 = 1120
    chromosome_length = y_axis1 + 80
    label_sex(x_axis1, x_axis2, sex)
    for j in range(y_axis1, chromosome_length):
        x_variation = r.choice(range(-2, 3))
        x2_variation = r.choice(range(-2, 3))
        x_axis1 += x_variation
        x_axis2 += x2_variation
        x_chromosome1 = GOval(SIZE, SIZE, x=x_axis1, y=j)
        x_chromosome1.color = 'darkgray'
        x_chromosome2 = GOval(SIZE, SIZE, x=x_axis2, y=j)
        x_chromosome2.color = 'darkgray'
        chromosome_density = r.choice(range(10))
        if chromosome_density < 8:
            window.add(x_chromosome1)
            if sex == "F":
                window.add(x_chromosome2)
    if sex == "M":
        for k in range(y_axis1 + 50, chromosome_length):
            y_variation = r.choice(range(-2, 3))
            x_axis2 += y_variation
            y_chromosome = GOval(SIZE, SIZE, x=x_axis2, y=k)
            y_chromosome.color = 'darkgray'
            chromosome_density = r.choice(range(10))
            if chromosome_density < 8:
                window.add(y_chromosome)


def y_start(i):
    """
    This function will decide the start of y axis at each line.
    """
    y_axis = -180 + i * 200
    return y_axis


def label_n(i, pair_n, j, y_axis):
    """
    This function will put the number of each pair of chromosome at the bottom of the pair.
    """
    label = GLabel(pair_n, x=j + 25, y=y_axis + 210 - i * 30)
    return label


def label_sex(x_axis1, x_axis2, sex):
    """
    This function will put X or Y at the bottom of X or Y chromosome.
    """
    label_x1 = GLabel('X')
    label_x1.font = '-16'
    label_x2 = GLabel('X')
    label_x2.font = '-16'
    label_y = GLabel('Y')
    label_y.font = '-16'
    window.add(label_x1, x_axis1, y=710)
    if sex == "F":
        window.add(label_x2, x_axis2, y=710)
    if sex == "M":
        window.add(label_y, x_axis2, y=710)


def title(sex):
    """
    This function will generate the title of the painting.
    """
    if sex == "F":
        title_f = GLabel('Human Karyotype (Female)', x=420, y=800)
        title_f.font = '-40'
        window.add(title_f)
    if sex == "M":
        title_m = GLabel('Human Karyotype (Male)', x=450, y=800)
        title_m.font = '-40'
        window.add(title_m)


if __name__ == '__main__':
    main()
