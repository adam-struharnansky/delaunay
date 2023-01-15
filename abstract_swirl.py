import colors as c
import turtle
import random
from myTurtle_A import *

previous = []


def generate_color(step):
    col = c.any_swirl()
    if step == 0:
        while col == c.swirl_white():
            col = c.any_swirl()
    return col


def draw_circle(t: MyTurtle_A, radius: int, angle: int, step: int):
    col = generate_color(step)
    while col in previous:
        col = generate_color(step)
    previous.append(col)

    t.color(col)
    t.begin_fill()
    t.circle(radius, angle)
    pos = t.position()
    head = t.heading()
    t.left(90)
    t.fd(radius)
    t.end_fill()
    t.jump_to(pos)
    t.setheading(head)

    col = generate_color(step)
    while col in previous:
        col = generate_color(step)
    previous.append(col)

    t.color(col)
    t.begin_fill()
    t.circle(radius, 360 - angle)
    pos = t.position()
    head = t.heading()
    t.left(90)
    t.fd(radius)
    t.end_fill()
    t.jump_to(pos)
    t.setheading(head)


def abstract_swirl(t: MyTurtle_A, radius: int):
    global previous
    turtle.bgcolor(c.swirl_white())
    for i in range(10):
        t.jump_to(0, 0)
        t.setheading(180)
        t.jump_by(0, radius)
        draw_circle(t, radius, random.randint(60, 300), i)
        radius -= random.randint(10, 35)
        if i > 0:
            previous = previous[-2:]

    t.color(c.any_swirl())
    t.jump_to(0, 0)
    t.setheading(180)
    t.jump_by(0, radius)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

    t.setheading(180)
    t.jump_to(0, -45)
    t.color(c.any_swirl())
    t.begin_fill()
    t.circle(110, 180)
    t.end_fill()

    t.setheading(0)
    t.jump_to(0, 45)
    t.color(c.any_swirl())
    t.begin_fill()
    t.circle(110, 180)
    t.end_fill()

