#Write the definition of a Point class. Objects from this class should have:
#a method show to display the coordinates of the point
#a method move to change these coordinates
#a method dist that computes the distance between 2 points

import math

class Point():

    pointsHor = []
    pointsVer = []

    def __init__(self, hor=0, ver=0):
        self.hor = hor
        self.ver = ver

    def add(self):
        print("You are adding a point \n")
        self.hor = int(input("Enter a horizontal position: "))
        self.pointsHor.append(self.hor)
        self.ver = int(input("Enter a vertical position: "))
        self.pointsVer.append(self.ver)
    
    def move(self, pointSlot):
        print(f"You are changing a point number {pointSlot + 1}\n")
        self.pointsHor[pointSlot] = int(input("Enter a horizontal position: "))
        self.pointsVer[pointSlot] = int(input("Enter a vertical position: "))
    
    #Here I don't use the user input in sake of showing that I can pass arguments to the method
    def dist(self, firtsPoint, secondPoint):
        self.firstPoint = firtsPoint
        self.secondPoint = secondPoint

        self.firstPoint = [self.pointsHor[self.firstPoint], self.pointsVer[self.firstPoint]]
        self.secondPoint = [self.pointsHor[self.secondPoint], self.pointsVer[self.secondPoint]]

        return f"The distance between point {firtsPoint + 1} and {secondPoint + 1} is: {math.dist(self.firstPoint, self.secondPoint)}\n"

    def show(self):
        return f"Horisontal: {self.hor} \nVertical: {self.ver}\n"

    def drop(self):
        del(self.pointsHor[:])
        del(self.pointsVer[:])
        print("All points were deleted\n")


#Creating an object from the Point() class
point = Point()

#Executing all methods in a meaningfull order
point.add()
print(point.show())

point.add()
print(point.show())

print(point.dist(0, 1))

point.move(1)

print(point.dist(0, 1))

point.drop()