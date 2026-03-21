import random
number = random.randint(1,10)
guess = int(input("guess between 1 to 10 : "))
while guess != number:
    if guess < number:
        print("Too low! try again")
    else:
        print("Too high! try again")
    guess= int(input("guess between 1 to 10 : "))
print("Congratulations.........!!")