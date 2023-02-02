#Sets

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
    print("Yes, apple is a fruit!")
#we are adding operator "in" to check if the element is in the collection

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
#we are adding element "orange" to the set using the "add()" method

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
#we are adding multiple elements to the collection using the "update()" method

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
#we are removing element "banana" from the collection using "remove()" method

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
#we are removing element "banana" from the collection using the discard method