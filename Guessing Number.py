import random
import math
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
x = random.randint(lower, upper)
total_chances = 10
print("\n\tYou've only ", total_chances, " chances to guess the integer!\n")
count = 0
flag = False
while count < total_chances:
    count += 1
    guess = int(input("Guess a number:- "))
    if x == guess:
        print("Congratulations you did it in ",count, " try")
        flag = True
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
if not flag:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")