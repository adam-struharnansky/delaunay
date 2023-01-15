import random

from myColor import MyColor
from auxiliary_math import half_circle
from colors import random_hsv
from rythme_line_delaunay import circle_delaunay


CIRCLE_POINTS = 60
RANDOM_CIRCLES_RATIO = 2 / 3
COLORS = 3


def rythme_area_delaunay(t: object, start: tuple, columns: int, rows: int, side: float) -> None:
    # background
    for i in range(0, rows):
        for j in range(0, columns):
            if (i % 3 == 2 and j % 3 == 2) or (i == 0 and j % 3 == 2) or (i % 3 == 2 and j == 0) or (i == 0 and j == 0):
                edge = (i * side + start[0], j * side + start[1])
                color = random_hsv()
                t.ptsGon([edge, (edge[0], edge[1] + 3 * side), (edge[0] + 3 * side, edge[1] + 3 * side),
                         (edge[0] + 3 * side, edge[1] + 3 * side), (edge[0] + 3 * side, edge[1])], color, color)

    t.ptsGon([(start[0] + columns * side, start[1]), (start[0] + (columns + 3) * side, start[1]),
              (start[0] + (columns + 3) * side, start[1] + (rows + 3) * side),
              (start[0] + columns * side, start[1] + (rows + 3) * side)], MyColor('white'), MyColor('white'))
    t.ptsGon([(start[0], start[1] + rows * side), (start[0] + columns * side, start[1] + rows * side),
              (start[0] + (columns + 3) * side, start[1] + (rows + 3) * side),
              (start[0], start[1] + (rows + 3) * side)], MyColor('white'), MyColor('white'))

    colors = []
    for _ in range(0, COLORS):
        colors.append(random_hsv())

    for _ in range(0, int(RANDOM_CIRCLES_RATIO * rows * columns)):
        centre = ((random.randrange(0, columns // 3) * 3 + 2) * side + start[0],
                  (random.randrange(0, rows // 3) * 3 + 2) * side + start[1])
        direction = random.randrange(0, 4)
        color = colors[random.randrange(0, COLORS)]
        if direction == 0:
            t.ptsGon(half_circle(centre, (centre[0] + 2 * side, centre[1]), CIRCLE_POINTS), color, color)
        elif direction == 1:
            t.ptsGon(half_circle(centre, (centre[0] - 2 * side, centre[1]), CIRCLE_POINTS), color, color)
        elif direction == 2:
            t.ptsGon(half_circle(centre, (centre[0], centre[1] + 2 * side), CIRCLE_POINTS), color, color)
        elif direction == 3:
            t.ptsGon(half_circle(centre, (centre[0], centre[1] + 2 * side), CIRCLE_POINTS), color, color)

    for i in range(0, rows // 3):
        for j in range(0, columns // 3):
            centre = ((3 * i + 2) * side + start[0], (3 * j + 2) * side + start[1])
            circle_delaunay(t, centre, side, [MyColor('black'), MyColor('white')])
