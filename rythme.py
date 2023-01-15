import random

from myTurtle_A import *
import colors as c

three = []
coordinates = [(0, 280), (0, 0), (0, -280)]


def draw_circle(t: MyTurtle_A, radius: float, angle: float) -> None:
    t.begin_fill()
    t.circle(radius, angle)
    h = t.heading()
    pos = t.position()
    t.left(90)
    t.fd(radius)
    t.end_fill()
    t.setheading(h)
    t.jump_to(pos)


def background(t: MyTurtle_A, bg_radius: float) -> None:
    t.setheading(180)
    t.jump_to(0, bg_radius + 50)
    top = 400
    radius = bg_radius
    for i in range(8):
        t.color(c.random_hsv())
        draw_circle(t, radius, 180)
        change = random.randint(5, 40)
        radius -= change
        top -= change
        t.jump_to(0, top)
        t.setheading(180)

    radius = bg_radius
    t.setheading(0)
    t.jump_to(0, -(bg_radius + 50))
    top = -400
    for i in range(8):
        t.color(c.random_hsv())
        draw_circle(t, radius, 180)
        change = random.randint(5, 40)
        radius -= change
        top += change
        t.jump_to(0, top)
        t.setheading(0)


def top_three(t: MyTurtle_A) -> None:
    t.jump_to(0, 0)
    for i in range(28):
        area = random.randint(0, 2)
        t.jump_to(coordinates[area])
        whole = random.randint(0, 1)
        t.setheading(180)
        if whole == 1:
            t.jump_by(0, three[area])
            t.color(c.random_hsv())
            draw_circle(t, three[area], 360)

        else:
            two_halfs = random.randint(0, 1)
            if two_halfs == 1:
                t.jump_by(0, three[area])
                t.color(c.random_hsv())
                draw_circle(t, three[area], 180)
                t.color(c.random_hsv())
                draw_circle(t, three[area], 180)

            else:
                right = 1
                if right == 0:
                    t.jump_by(0, three[area])
                    t.color(c.random_hsv())
                    draw_circle(t, three[area], 180)

                else:
                    t.setheading(0)
                    t.jump_by(0, -three[area])
                    t.color(c.random_hsv())
                    draw_circle(t, three[area], 180)

        change = random.randint(5, 22)
        three[area] -= change


def rythme(t: MyTurtle_A, bg_radius: float, top_radius: float) -> None:
    background(t, bg_radius)
    for i in range(3):
        three.append(top_radius)
    top_three(t)
