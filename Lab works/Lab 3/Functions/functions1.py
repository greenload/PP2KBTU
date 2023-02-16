import math
#A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces.
#Create a function to convert grams to ounces. ounces = 28.3495231 * grams

def to_grams(ounces):
    grams = 28.3495231 * ounces
    return float(grams)

#Read in a Fahrenheit temperature. Calculate and display the equivalent centigrade temperature.
#The following formula is used for the conversion: C = (5 / 9) * (F – 32)

def far_to_cels(far):
    cels = (5/9) * (far - 32)
    
    print(f"Celsius is: {cels}")
    return cels

#Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm.
#How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):

def solve(numheads: int, numlegs: int):
    
    if numlegs < numheads * 2:
        print("It should be enough legs at least for chicks.")
        return False, False
    elif  numlegs % 2 != 0:
        print("Quantity of legs should be even.")
        return False, False
    elif numlegs > numheads * 4:
        print(f"It should be not more then {numheads*4} legs for {numheads} heads.")
        return False, False
    else:
        rabbits = (numlegs - (numheads * 2)) / 2
        chicks = numheads - rabbits
    return rabbits, chicks

#You are given list of numbers separated by spaces.
#Write a function filter_prime which will take list of numbers as an agrument and returns only prime numbers from the list.

def filter_prime():



    return primes

#Write a function that accepts string from user and print all permutations of that string.



#Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We



#Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
""""
def has_33(nums):
    pass

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False

#Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    pass

spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
"""



#Write a function that computes the volume of a sphere given its radius.

def volume(radius: int):

    volume = 4/3 * math.pi() * radius**3

    return volume

#Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Note: don't use collection set.



#Write a Python function that checks whether a word or phrase is palindrome or not.
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam



#Define a functino histogram() that takes a list of integers and prints a histogram to the screen.
#For example, histogram([4, 9, 7]) should print the following:



#Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20.
#This is how it should work when run in a terminal:
""""
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!
"""



#Create a python file and import some of the functions from the above 13 tasks and try to use them.
"""
I created several files for different functions, working as mini programs. All of them are in this directory
"""