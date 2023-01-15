from myColor import *
import random


def swirl_green() -> MyColor:
    return MyColor(113, 150, 34)


def swirl_blue() -> MyColor:
    return MyColor(0, 80, 117)


def swirl_red() -> MyColor:
    return MyColor(184, 30, 28)


def swirl_white() -> MyColor:
    return MyColor(180, 183, 190)


def swirl_black() -> MyColor:
    return MyColor(13, 14, 21)


def any_swirl() -> MyColor:
    return [swirl_green(), swirl_blue(), swirl_red(), swirl_white(), swirl_black()][random.randrange(0, 5)]


def random_hsv() -> MyColor:
    return MyColor(h=random.randint(0, 359), s=random.randint(26, 230), v=random.randint(205, 255))
