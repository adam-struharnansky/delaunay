import math


TRIANGLE_THRESHOLD = 1


def triangle_points_area(a: tuple, b: tuple, c: tuple) -> float:
    return abs(((b[0] - a[0]) * (c[1] - a[1]) - (c[0] - a[0]) * (b[1] - a[1])) / 2)


def triangle_area(points: list) -> float:
    return triangle_points_area(points[0], points[1], points[2])


def polygon_area(points: list) -> float:
    if len(points) < 3:
        return 0
    if len(points) == 3:
        return triangle_area(points)
    points.pop()
    return triangle_area([points[-2], points[-1], points[0]]) + polygon_area(points)


def length(a: tuple, b: tuple) -> float:
    return math.sqrt((a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]))


def inside_triangle(point: tuple, triangle: list) -> bool:
    area_a = triangle_points_area(point, triangle[1], triangle[2])
    area_b = triangle_points_area(point, triangle[0], triangle[2])
    area_c = triangle_points_area(point, triangle[0], triangle[1])
    return abs(area_a + area_b + area_c - triangle_area(triangle)) < TRIANGLE_THRESHOLD


def inside(point: tuple, polygon: list) -> bool:
    if len(polygon) < 3:
        return False
    if inside_triangle(point, [polygon[-2], polygon[-1], polygon[0]]):
        return True
    polygon.pop()
    return inside(point, polygon)
