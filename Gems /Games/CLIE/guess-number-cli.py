import random

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    previous_guesses = []

    print("\nWelcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")
    print("Can you guess it?\n")

    while attempts < max_attempts:
        # Get player's guess
        try:
            guess = input(f"Attempt {attempts + 1}/{max_attempts}. Enter your guess: ")
            guess = int(guess)

            # Validate input
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            if guess in previous_guesses:
                print("You already tried that number! Try something else.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        # Track the attempt
        attempts += 1
        previous_guesses.append(guess)

        # Check the guess
        if guess == secret_number:
            print(f"\nCongratulations! You've guessed the number in {attempts} attempts!")
            return True
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        # Show remaining attempts
        if attempts < max_attempts:
            print(f"You have {max_attempts - attempts} attempts remaining.")

        # Show previous guesses
        print(f"Your previous guesses: {sorted(previous_guesses)}\n")

    print(f"\nGame Over! The number was {secret_number}.")
    return False

def main():
    score = 0
    while True:
        if play_game():
            score += 1

        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"\nThanks for playing! You won {score} game(s)!")
            break

if __name__ == "__main__":
    main()
