# Day 5: Number Guessing Game

secret_number = 7

guess = int(input("Guess the number (between 1 and 10):"))

if guess == secret_number:
    print("Congratulations! YOu guessed it right.")
elif guess > secret_number:
    print("Too high! Try again.")
else:
    print("Too low! TRy again.")
