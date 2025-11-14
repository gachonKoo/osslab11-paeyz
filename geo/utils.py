import math

def distance(x1, y1, x2, y2):
    result = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(result, 2)

def area_triangle(base, height):
    result = 0.5 * base * height
    return round(result, 2)

def circle_area(radius):
    result = math.pi * radius ** 2
    return round(result, 2)
