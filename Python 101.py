import random

def charLevel():
    while True:
        try:
            level = int(input("Choose a level from 1-10. The higher you go, the more difficult it will be: "))

            if level > 10 or level < 1:
                print("Your level must be between 1 and 10.")
            else:
                difficulty = 1000 // level
                return difficulty

        except ZeroDivisionError:
            return 1000

        except ValueError:
            print("Please enter a whole number (no decimals).")


def charChoice():
    characters = [
        "Peely (from Fortnite)",
        "Mario (from the Super Mario series)",
        "Pikachu (from Pokémon)"
    ]
    return random.choice(characters)


def playGame(difficulty, character):
    print("You are playing as {character}!")
    print("Difficulty setting: {difficulty} (lower means harder).")

    secret_number = random.randint(1, difficulty)
    print("A wild challenge appears! Guess the secret number between 1 and {difficulty}.")

    attempts = 3
    while attempts > 0:
        try:
            guess = int(input("Your guess: "))

            if guess == secret_number:
                print("🎉 Congratulations! You won the challenge!")
                return

            attempts -= 1
            if attempts > 0:
                print("Wrong guess! Try again. Attempts left: {attempts}")
            else:
                print("Game Over! The secret number was {secret_number}.")

        except ValueError:
            print("Please enter a valid number.")


print("Welcome to the Mini Adventure Game!")
difficulty = charLevel()
character = charChoice()
playGame(difficulty, character)




