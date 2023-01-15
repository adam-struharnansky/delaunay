import random
import math
from copy import deepcopy

from myColor import MyColor
from auxiliary_math import polygon_area, length, extreme, fit_circle_in_rectangle, circle, half_circle
from colors import random_hsv


CIRCLE_POINTS = 60
RANDOM_CIRCLES_RATIO = 2 / 3


def circle_delaunay(t, centre, radius, colors):
    if random.uniform(0, 1) < 1 / 2:
        circle_color = colors[random.randrange(0, len(colors))]
        t.ptsGon(circle(centre, radius, CIRCLE_POINTS), circle_color, circle_color)
    else:
        first_color = colors[random.randrange(0, len(colors))]
        second_color = colors[random.randrange(0, len(colors))]
        if random.uniform(0, 1) < 1 / 2:
            t.ptsGon(half_circle(centre, (centre[0], centre[1] - radius), CIRCLE_POINTS), first_color, first_color)
            t.ptsGon(half_circle(centre, (centre[0], centre[1] + radius), CIRCLE_POINTS), second_color, second_color)
            if random.uniform(0, 1) < 3 / 4:
                t.ptsGon(half_circle(centre, (centre[0], centre[1] - radius / 2), CIRCLE_POINTS), second_color,
                         second_color)
                t.ptsGon(half_circle(centre, (centre[0], centre[1] + radius / 2), CIRCLE_POINTS), first_color,
                         first_color)
        else:
            t.ptsGon(half_circle(centre, (centre[0] - radius, centre[1]), CIRCLE_POINTS), first_color, first_color)
            t.ptsGon(half_circle(centre, (centre[0] + radius, centre[1]), CIRCLE_POINTS), second_color, second_color)
            if random.uniform(0, 1) < 3 / 4:
                t.ptsGon(half_circle(centre, (centre[0] - radius / 2, centre[1]), CIRCLE_POINTS), second_color,
                         second_color)
                t.ptsGon(half_circle(centre, (centre[0] + radius / 2, centre[1]), CIRCLE_POINTS), first_color,
                         first_color)


def rythme_line_delaunay(t, start, end, segments):
    segments = segments * 3
    vector = ((end[0] - start[0]) / segments, (end[1] - start[1]) / segments)
    segment_length = length(start, end) / segments

    # najskor to prejst z vacsimi, potom z mensimi kruhmi, ktore budu na vrchu
    for _ in range(0, segments // 3):
        segment = random.randrange(1, segments - 1)
        centre = (start[0] + segment * vector[0], start[1] + segment * vector[1])
        number = random.randint(2, 5)
        for i in range(0, number):
            color = random_hsv()
            t.ptsGon(circle(centre, segment_length * (number - i), CIRCLE_POINTS), color, color)

    base_color = random_hsv()
    for i in range(0, segments):
        if i % 3 == 1:
            centre = (start[0] + i * vector[0], start[1] + i * vector[1])
            t.ptsGon(circle(centre, segment_length * 2, CIRCLE_POINTS), base_color, base_color)

    line_color = MyColor(h=base_color.h + [60, -60][random.randrange(0, 2)], s=base_color.s, v=base_color.v)
    line_color = line_color.closeHSV(h=20, s=10, v=10)
    for i in range(0, segments):
        if i % 3 == 1:
            centre = (start[0] + i * vector[0], start[1] + i * vector[1])
            direction = [-1, 1][random.randint(0, 1)]
            second_point = (centre[0] + direction * vector[0] * 2, centre[1] + direction * vector[1] * 2)
            t.ptsGon(half_circle(centre, second_point, CIRCLE_POINTS), line_color, line_color)

    for i in range(0, segments):
        if i % 3 == 1:
            centre = (start[0] + i * vector[0], start[1] + i * vector[1])
            circle_delaunay(t, centre, segment_length / 2, [MyColor('white'), MyColor('black')])

    pass
