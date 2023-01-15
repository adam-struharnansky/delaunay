import random
import turtle

from myTurtle_A import *
from myColor import *
from simple_recursive_delaunay import simple_recursive_dalaunay
from abstract_swirl import abstract_swirl
from rythme import rythme


t = MyTurtle_A()
t.speed(0)
tracer(0)
delay(0)

# simple_recursive_dalaunay(t, [(-200, -200), (-200, 200), (200, 200), (200, -200)], 0)
# simple_recursive_dalaunay(t, [(-200, -200), (-200, 0), (-200, 200), (200, 200), (200, 0), (200, -200)], 0)
# abstract_swirl(t, 300)
# rythme(t, 350, 140)

turtle.done()
