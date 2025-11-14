from geo import utils

# 거리: (0,0) → (3,4)
c = utils.distance(0, 0, 3, 4)
print(f"c = {c}")

# 삼각형 넓이: 밑변 10, 높이 5
area = utils.area_triangle(10, 5)
print(f"area = {area}")

# 원 넓이: 반지름 10 → π*10² = 314.159...
area = utils.circle_area(10)
print(f"area = {area}")
