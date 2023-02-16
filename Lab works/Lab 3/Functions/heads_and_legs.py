import functions1

numheads = int(input("Please, enter the quantity of heads: "))
numlegs = int(input("Please, enter the quantity of legs: "))

rabbits, chicks = functions1.solve(numheads, numlegs)

if chicks != False:
    print(f"There are {chicks} chicks and {rabbits} rabbits on this farm.")