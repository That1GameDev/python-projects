import random

def get_random_number():
    return random.randint(1, 100)

def play_game():
    number = get_random_number()
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts!")
            break

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ")
        if again.lower() != "yes":
            print("Thanks for playing!")
            break

main()