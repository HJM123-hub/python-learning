import random

max_attempts = 7


def ask_play_again():
    play_again = input("Play again? y/n: ")
    return play_again == "y"


def get_guess():
    user_input = input("Guess a number between 1 and 100, or q to quit: ")

    if user_input == "q":
        return "q"

    return int(user_input)


def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while attempts < max_attempts:
        try:
            guess = get_guess()

            if guess == "q":
                print("Game quit.")
                guessed_correctly = True
                break

            attempts = attempts + 1

            if guess < secret_number:
                print("Too low.")
            elif guess > secret_number:
                print("Too high.")
            else:
                guessed_correctly = True
                print(f"Correct. The number was {secret_number}.")
                print(f"You guessed it in {attempts} attempts.")
                break

        except ValueError:
            print("Invalid input. Please enter a number.")

    if attempts == max_attempts and not guessed_correctly:
        print(f"Game over. The number was {secret_number}.")


while True:
    play_game()

    if not ask_play_again():
        break
