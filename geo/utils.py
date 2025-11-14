import math

def distance(x1, y1, x2, y2):
    """두 점 사이 거리 계산"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def area_triangle(base, height):
    """삼각형 넓이 계산"""
    return 0.5 * base * height

def circle_area(radius):
    """원의 넓이 계산"""
    return math.pi * radius**2

