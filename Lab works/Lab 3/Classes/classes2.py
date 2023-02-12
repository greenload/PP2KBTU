#Define a class named Shape and its subclass Square.
#The Square class has an init function which takes a length as argument.
#Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape():

    def __init__(self):
        pass


class Square(Shape):

    def __init__(self, length=0):
        self.length = length

    def area(self):
        
        self.length = int(input())
        
        areaValue = self.length * self.length

        areaText = "Square area is:  {}"

        print(areaText.format(areaValue))

#Define a class named Rectangle which inherits from Shape class from task 2.
#Class instance can be constructed by a length and width.
#The Rectangle class has a method which can compute the area.

class Rectangle(Shape):
    
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width
    
    def area(self):
        self.length = int(input())
        self.width = int(input())

        areaValue = self.length * self.width

        areaText = "Rectangle area is:  {}"

        print(areaText.format(areaValue))

square = Square()

square.area()

rectangle = Rectangle()

rectangle.area()




