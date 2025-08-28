import random
n = random.randint(1, 10)
Guess = int(input("Guess the number (1-10): "))

if Guess == n:
    print("Correct!")
else:
    print("Sorry, the number is: ",n)