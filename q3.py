import random
import math
while True:
    lower = int(input("Enter Lower bound: "))
 

    upper = int(input("Enter Upper bound: "))

    x = random.randint(lower, upper)
    print("\n\tYou've only ",round(math.log(upper - lower + 1, 2))," chances to guess the integer!\n")
 
    cnt = 1
    while cnt < math.log(upper - lower + 1, 2):
        cnt += 1
        guess = int(input("Enter your number:- "))

        if x == guess:
            print("Congratulations!!")
            print("\nThe number is %d" % x)
            break
        elif x > guess:
            print("You guessed small!")
        elif x < guess:
            print("You Guessed high!")
 
    if cnt >= math.log(upper - lower + 1, 2):
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")
 
    print("Do you want to play again? (Y/N)")
    ans = input()
 
    if ans == 'n' or ans == 'N':
        break
     
print("\nThanks for playing")