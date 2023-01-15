import random

from myColor import MyColor, any
from auxiliary_math import half_circle, extreme, length, fit_circle_in_rectangle, circle


IMPORTANT_POINTS_NUMBER = 15
CIRCLES_NUMBER = 10
CIRCLE_POINTS = 60
MAXIMUM_TRIES = 400
HALF_TO_FULL_RATIO = 1/6
MIN_AREA = 15000


def divided_circles_delaunay(t: object, points: list) -> None:
    i_a = random.randrange(0, len(points) // 2)
    i_b = random.randrange(len(points) // 2, len(points))
    vector_a = (points[i_a - 1][0] - points[i_a][0], points[i_a - 1][1] - points[i_a][1])
    vector_b = (points[i_b - 1][0] - points[i_b][0], points[i_b - 1][1] - points[i_b][1])
    a = (points[i_a][0] + vector_a[0] * random.uniform(0, 1), points[i_a][1] + vector_a[1] * random.uniform(0, 1))
    b = (points[i_b][0] + vector_b[0] * random.uniform(0, 1), points[i_b][1] + vector_b[1] * random.uniform(0, 1))
    vector_m = (b[0] - a[0], b[1] - a[1])
    important_points = []
    for _ in range(0, IMPORTANT_POINTS_NUMBER):
        scale = random.uniform(0, 1)
        point = (a[0] + vector_m[0] * scale, a[1] + vector_m[1] * scale)
        important_points.append(point)
    list.sort(important_points)

    color_1 = MyColor(h=random.randrange(0, 360), s=random.randrange(0, 255), v=random.randrange(0, 255))
    color_2 = color_1.closeHSV(40, 40, 40)

    t.ptsGon(points[0:i_a] + [a, b] + points[i_b:len(points)], color_1, color_1)
    t.ptsGon(points[i_a:i_b] + [b, a], color_2, color_2)

    created_half_circles = 0
    tries = 0
    min_x = extreme(points, 0, min)
    min_y = extreme(points, 1, min)
    max_x = extreme(points, 0, max)
    max_y = extreme(points, 1, max)

    while created_half_circles < CIRCLES_NUMBER and tries < MAXIMUM_TRIES:
        a = important_points[random.randrange(0, IMPORTANT_POINTS_NUMBER)]
        b = important_points[random.randrange(0, IMPORTANT_POINTS_NUMBER)]
        radius = length(a, b)
        color = any()
        if fit_circle_in_rectangle(a, radius, min_x, min_y, max_x, max_y):
            if random.uniform(0, 1) < HALF_TO_FULL_RATIO:
                t.ptsGon(half_circle(a, b, CIRCLE_POINTS), color, color)
            else:
                t.ptsGon(circle(a, radius, CIRCLE_POINTS), color, color)
            created_half_circles += 1
        if fit_circle_in_rectangle(b, radius, min_x, min_y, max_x, max_y):
            if random.uniform(0, 1) < HALF_TO_FULL_RATIO:
                t.ptsGon(half_circle(b, a, CIRCLE_POINTS), color, color)
            else:
                t.ptsGon(circle(b, radius, CIRCLE_POINTS), color, color)
            created_half_circles += 1
        tries += 1
