import math

def calculate_circumference(radius):
    return 2 * math.pi * radius

def calculate_area(radius):
    return math.pi * radius ** 2

a = int(input())
radius = a
circumference = calculate_circumference(radius)
area = calculate_area(radius)

print(f"Длина окружности: {circumference}")
print(f"Площадь круга: {area}")