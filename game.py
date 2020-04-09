import random

number = random.randrange(1,10)
guess = int(input("\nGuess a number between 1 to 10: "))

while guess != number:
    if guess < number:
        print("Try again! Guess a higher number")
    guess = int(input("\nGuess a number between 1 to 10: "))

else:
    print("Try again! Guess a lower number")
    guess = int(input("\nGuess a number between 1 to 10: "))

print("You Have Won!!!")
