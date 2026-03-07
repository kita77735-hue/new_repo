import math


def square(side):
    return math.ceil(side ** 2)


side = int(input("введите длину стороны "))
print(f"Площадь квадрата: {square(side)}")
