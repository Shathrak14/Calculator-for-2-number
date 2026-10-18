
import random

print("================================")
print("     NUMBER GUESSING GAME")
print("================================")
print("I have selected a number between 1 and 100.")
print("Can you guess it?")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100!")

        elif guess < secret_number:
            print("Too low! Try a bigger number.")

        elif guess > secret_number:
            print("Too high! Try a smaller number.")

        else:
            print("\nCongratulations! You guessed it!")
            print("The secret number was:", secret_number)
            print("Number of attempts:", attempts)
            break

    except ValueError:
        print("Invalid input! Please enter a whole number.")
