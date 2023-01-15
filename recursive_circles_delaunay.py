import random
from copy import deepcopy

from myColor import MyColor
from auxiliary_math import polygon_area, length, extreme, fit_circle_in_rectangle, circle, half_circle


MIN_AREA = 80000
CIRCLE_POINTS = 60
IMPORTANT_POINTS_NUMBER = 7
CIRCLES_NUMBER = 12
TRIES_NUMBER = 200


def recursive_circles_delaunay(t: object, points: list, color: MyColor) -> None:
    if polygon_area(deepcopy(points)) < MIN_AREA:
        color = color.closeHSV(h=30, s=10, v=10)
        t.ptsGon(points, color, color)
        return
    i_a = random.randrange(0, len(points) // 2)
    i_b = random.randrange(len(points) // 2, len(points))
    vector_a = (points[i_a - 1][0] - points[i_a][0], points[i_a - 1][1] - points[i_a][1])
    vector_b = (points[i_b - 1][0] - points[i_b][0], points[i_b - 1][1] - points[i_b][1])
    scale_a, scale_b = random.uniform(0, 1), random.uniform(0, 1)
    a = (points[i_a][0] + vector_a[0] * scale_a, points[i_a][1] + vector_a[1] * scale_a)
    b = (points[i_b][0] + vector_b[0] * scale_b, points[i_b][1] + vector_b[1] * scale_b)

    color_1 = MyColor(h=color.h + [-60, 60][random.randrange(0, 1)], s=color.s, v=color.v)
    color_1 = color_1.closeHSV(h=10, s=10, v=10)
    color_2 = MyColor(h=color.h + [-60, 60][random.randrange(0, 1)], s=color.s, v=color.v)
    color_2 = color_2.closeHSV(h=10, s=10, v=10)
    recursive_circles_delaunay(t, points[0:i_a] + [a, b] + points[i_b:len(points)], color_1)
    recursive_circles_delaunay(t, points[i_a:i_b] + [b, a], color_2)

    vector_m = (b[0] - a[0], b[1] - a[1])
    important_points = []
    for _ in range(0, IMPORTANT_POINTS_NUMBER):
        scale = random.uniform(0, 1)
        point = (a[0] + vector_m[0] * scale, a[1] + vector_m[1] * scale)
        important_points.append(point)
    list.sort(important_points)

    circles_number = 0
    tries = 0
    min_x = extreme(points, 0, min)
    min_y = extreme(points, 1, min)
    max_x = extreme(points, 0, max)
    max_y = extreme(points, 1, max)
    while circles_number < CIRCLES_NUMBER // 2 and tries < TRIES_NUMBER:
        a = important_points[random.randrange(0, IMPORTANT_POINTS_NUMBER)]
        b = important_points[random.randrange(0, IMPORTANT_POINTS_NUMBER)]
        radius = length(a, b)
        if fit_circle_in_rectangle(a, radius, min_x, min_y, max_x, max_y):
            circle_color = MyColor(h=color.h + [-60, 60][random.randrange(0, 1)], s=color.s, v=color.v)
            circle_color = circle_color.closeHSV(h=40, s=10, v=10)
            t.ptsGon(circle(a, radius, CIRCLE_POINTS), circle_color, circle_color)
            circles_number += 1
            if random.randrange(0, 1) < 1 / 2:
                circle_color = MyColor(h=circle_color.h + [-60, 60][random.randrange(0, 1)], s=circle_color.s,
                                       v=circle_color.v)
                t.ptsGon(circle(a, radius / 2, CIRCLE_POINTS), circle_color, circle_color)
        tries += 1
    while circles_number < CIRCLES_NUMBER and tries < TRIES_NUMBER:
        a = important_points[random.randrange(0, IMPORTANT_POINTS_NUMBER)]
        b = important_points[random.randrange(0, IMPORTANT_POINTS_NUMBER)]
        radius = length(a, b)
        if fit_circle_in_rectangle(a, radius, min_x, min_y, max_x, max_y):
            first_color = MyColor(h=color.h + [-60, 60][random.randrange(0, 1)], s=color.s, v=color.v)
            first_color = first_color.closeHSV(h=40, s=10, v=10)
            t.ptsGon(half_circle(a, b, CIRCLE_POINTS), first_color, first_color)
            second_color = MyColor(h=color.h + [-120, 120][random.randrange(0, 1)], s=color.s, v=color.v)
            second_color = second_color.closeHSV(h=40, s=10, v=10)
            second_point = (a[0] - (b[0] - a[0]), a[1] - (b[1] - a[1]))
            t.ptsGon(half_circle(a, second_point, CIRCLE_POINTS), second_color, second_color)
            circles_number += 1
            if random.randrange(0, 1) < 1 / 2:
                second_point = ((second_point[0] + a[0]) / 2, (second_point[1] + a[1]) / 2)
                t.ptsGon(half_circle(a, second_point, CIRCLE_POINTS), first_color, first_color)
                second_point = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
                t.ptsGon(half_circle(a, second_point, CIRCLE_POINTS), second_color, second_color)
        tries += 1
