import random
import math
from copy import deepcopy

from auxiliary_math import polygon_area, length, inside
from myColor import any


MIN_AREA = 15000
CIRCLE_RATIO = 1 / 3
CIRCLE_POINTS = 100
GAP_CIRCLE_RATIO = 1/10


def simplified_polygon_circle_intersection(polygon: list, centre: tuple, radius: float) -> list:
    result = []
    inside_circle = []
    for point in polygon:
        if length(point, centre) < radius:
            inside_circle.append(point)
    for i in range(0, CIRCLE_POINTS):
        angle = 2 * math.pi * i / CIRCLE_POINTS
        point = (radius * math.cos(angle) + centre[0], radius * math.sin(angle) + centre[1])
        if inside(point, deepcopy(polygon)):
            result.append(point)
        else:
            result = result + inside_circle
            inside_circle = []
    return result


def simple_recursive_dalaunay(t: object, points: list, area_change: float) -> None:
    if len(points) < 3:
        return
    if polygon_area(deepcopy(points)) + area_change < MIN_AREA:
        color = any()
        t.ptsGon(points, color, color)
        return
    if random.uniform(0, 1) > CIRCLE_RATIO:
        if len(points) > 3:
            a = random.randrange(0, len(points) // 2)
            b = random.randrange(len(points) // 2, len(points))
            first = points[0:a + 1] + points[b:len(points)]
            second = points[a:b + 1]
            simple_recursive_dalaunay(t, first, area_change)
            simple_recursive_dalaunay(t, second, area_change)
        elif len(points) == 3:
            point_index = random.randrange(0, 3)
            new_point = ((points[point_index][0] + points[point_index - 1][0]) / 2,
                         (points[point_index][1] + points[point_index - 1][1]) / 2)
            first = [new_point, points[point_index - 2], points[point_index]]
            second = [new_point, points[point_index - 2], points[point_index - 1]]
            simple_recursive_dalaunay(t, first, area_change)
            simple_recursive_dalaunay(t, second, area_change)
    else:
        a = points[random.randrange(0, len(points) // 2)]
        b = points[random.randrange(len(points) // 2, len(points))]
        centre = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
        side = length(a, b)
        radius = random.uniform(side * GAP_CIRCLE_RATIO, side * (1 - GAP_CIRCLE_RATIO)) / 2
        circle_area = math.pi * radius * radius
        simple_recursive_dalaunay(t, points, area_change - circle_area)
        simple_recursive_dalaunay(t, simplified_polygon_circle_intersection(points, centre, radius), 0)
