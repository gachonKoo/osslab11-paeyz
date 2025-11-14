import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def area_triangle(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

