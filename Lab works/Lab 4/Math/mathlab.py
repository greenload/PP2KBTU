import math

#Write a Python program to convert degree to radian.

def deg_to_rad(deg: int):
    rad = math.radians(deg)
    return rad

#Write a Python program to calculate the area of a trapezoid.

def trapezoid_area(height: float, firstBase: float, secondBase: float):
    area = ((firstBase + secondBase)/2) * height
    return area


#Write a Python program to calculate the area of regular polygon.
def polygon_area(sideQuantity: int, sideLength: int):

    perimeter = sideQuantity * sideLength
    apothem = sideLength / 2 * math.tan(math.radians(180)/sideQuantity)
    area = (perimeter * apothem)/2
    return math.ceil(area)

#Write a Python program to calculate the area of a parallelogram.
def parallelogram_area(baseLength: float, height: float):
    area = baseLength * height
    return area