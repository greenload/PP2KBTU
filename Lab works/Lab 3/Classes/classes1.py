#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.

class Stringer:

    def getString(self):
        self.phrase = input()

    def printString(self):
        print(self.phrase)

str = Stringer()
   
str.getString()
str.printString()