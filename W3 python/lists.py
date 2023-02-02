#Lists

fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#we are adding "fruits[1]" to pass the value of this element to "print" function

fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"
#we are adressing the first element with index "0" and changing its value to "kiwi"

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
#we are appending "orange" as an element to the list "fruits" by using an "append" function

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
#we are inserting "lemon" as an element of first index (2nd position) moving all other elements 1 position to the right

fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
#we are removing "banana" by using "remove" function which is serching for the first same value

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
#we are using negative indexing to addres the last element of the list to print it

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
#we are using index range from "2" to "5" to print values from the list with the third, fourth and fith positions

fruits = ["apple", "banana", "cherry"]
print(len(fruits))
#we are printiong the length of the list by using "len()" function to get it's length