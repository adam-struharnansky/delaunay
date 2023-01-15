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


def angle(centre: tuple, point_a: tuple, point_b: tuple) -> float:
    length_a = length(centre, point_b)
    length_b = length(centre, point_a)
    length_c = length(point_a, point_b)
    if length_a == 0.0 or length_b == 0.0:
        return 0.0
    cosine = (length_c ** 2 - length_a ** 2 - length_b ** 2) / (-2 * length_a * length_b)
    cosine = min(1.0, max(-1.0, cosine))
    return math.acos(cosine)


def half_circle(point_centre: tuple, point_edge: tuple, points_number: int) -> list:
    result = []
    ang = angle(point_centre, (point_centre[0], point_centre[1] - 40), point_edge)
    radius = length(point_centre, point_edge)
    if point_edge < point_centre:
        ang = -ang
    ang += math.pi / 2
    for i in range(points_number):
        current_angle = ang + i * math.pi / (points_number - 1)
        point = (point_centre[0] + radius * math.cos(current_angle), point_centre[1] + radius * math.sin(current_angle))
        result.append(point)
    return result


def circle(point_centre: tuple, radius: float, points_number: int) -> list:
    result = []
    for i in range(points_number):
        current_angle = i * 2 * math.pi / (points_number - 1)
        point = (point_centre[0] + radius * math.cos(current_angle), point_centre[1] + radius * math.sin(current_angle))
        result.append(point)
    return result


def extreme(points: list, coordinate: int, function: callable) -> object:
    result = points[0][coordinate]
    for point in points:
        result = function(result, point[coordinate])
    return result


def fit_circle_in_rectangle(centre: tuple, radius: float, min_x: float, min_y: float, max_x: float, max_y: float) \
        -> bool:
    x = centre[0] - radius > min_x and centre[0] + radius < max_x
    y = centre[1] - radius > min_y and centre[1] + radius < max_y
    return x and y
