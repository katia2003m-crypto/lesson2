import math


def square(side):
    area = side * side
    if isinstance(side, int):
        return area
    else:
        return math.ceil(area)


print("Площадь (сторона 5):", square(5))
print("Площадь (сторона 4.2):", square(4.2))
