import random

# Function to play the guessing game
def guessing_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != number_to_guess:
        guess = int(input("Make your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")

# Start the game
if __name__ == '__main__':
    guessing_game()