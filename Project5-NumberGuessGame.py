import random

def number_guessing_game():
    number = random.randint(1, 100)
    print("Guess a number between 1 and 100!")

    while True:
        guess = int(input("Your guess: "))
        if guess == number:
            print("Correct! You guessed the number.")
            break
        elif guess < number:
            print("Too low!")
        else:
            print("Too high!")

print(number_guessing_game())
