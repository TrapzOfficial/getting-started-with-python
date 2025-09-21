# guess_number.py
import random

def main():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 50)
    attempts = 0
    guess = 0

    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 50: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")

    print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")

if __name__ == "__main__":
    main()
