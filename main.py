import random
import turtle

from myTurtle_A import *
from myColor import *
from colors import random_hsv
from simple_recursive_delaunay import simple_recursive_dalaunay
from divided_circles_delaunay import divided_circles_delaunay
from abstract_swirl import abstract_swirl
from rythme import rythme
from recursive_circles_delaunay import recursive_circles_delaunay
from rythme_line_delaunay import rythme_line_delaunay
from rythme_area_delaunay import rythme_area_delaunay


t = MyTurtle_A()
t.speed(0)
tracer(0)
delay(0)

# simple_recursive_dalaunay(t, [(-200, -200), (-200, 200), (200, 200), (200, -200)], 0)
# simple_recursive_dalaunay(t, [(-200, -200), (-200, 0), (-200, 200), (200, 200), (200, 0), (200, -200)], 0)
# divided_circles_delaunay(t, [(-200, -200), (-200, 200), (200, 200), (200, -200)])
# abstract_swirl(t, 300)
rythme(t, 350, 140)
# recursive_circles_delaunay(t, [(-200, -200), (-200, 200), (200, 200), (200, -200)], random_hsv())
# rythme_line_delaunay(t, (0, 250), (0, -250), 8)
# rythme_area_delaunay(t, (-250, -250), 25, 25, 20)

turtle.done()
