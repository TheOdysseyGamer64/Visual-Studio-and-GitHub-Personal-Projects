#Definitions of all the functions. Main program starts below. Look to second comment on line 25.
import random
def charLevel():
    while True:
        try:
            level = int(input("Choose a level from 1-10. The higher you go, the more difficult it will be."))
            if level > 10 or level < 0:
                print("Your level selection should be from 1 to 10. It cannot exceed the limits. The sky is not the limit in games.")
            else:
                level = 1000 // level
                break
        except ZeroDivisionError:
            level = 1000
            break
        except ValueError:
            print("Make sure the level you give is not a decimal number. In simpler terms, make sure it's not a decimal number like 1.20 (which is the latest version of Minecraft)")
            return level

def charChoice():
    characters = ["Peely (from the famous shooter game Fortnite", "Mario (from the unmatched Super Mario Series)", "Pikachu (from the legendary Pokemon series)"]
    choice = random.choice(characters)
    return choice


#Main program starts here. Use the programming guide to help you if you are stuck. Good luck!
print("Choose a level from 1-10. The higher you go, the more difficult it will become.")
level = int(input("Choose a level from 1-10. The higher you go, the more difficult it will become."))
if level > 10 or level < 0:
    print("Your level selection must be between 1 and 10. You cannot exceed the limit. The sky is not the limit in games. In fact the game's coding boundaries are the limits. So stay in them.")
else:
    print("Please proceed to character selection. You can only choose between three characters as this game is not the one you hope for.")    


# Function to play a challenge
def playGame(difficulty, character):
    print(f"\nYou are playing as {character}!")
    print(f"Difficulty setting: {difficulty} (lower means harder).")

    # Simple challenge: guess a random number
    secret_number = random.randint(1, difficulty)
    print(f"\nA wild challenge appears! Guess the secret number between 1 and {difficulty}.")

    attempts = 3
    while attempts > 0:
        try:
            guess = int(input("Your guess: "))
            if guess == secret_number:
                print("🎉 Congratulations! You won the challenge!")
                return
            else:
                attempts -= 1
                if attempts > 0:
                    print(f"Wrong guess! Try again. Attempts left: {attempts}")
                else:
                    print(f"😢 Game Over! The secret number was {secret_number}.")
        except ValueError:
            print("Please enter a valid number.")

# Main program
print("Welcome to the Mini Adventure Game!")
difficulty = charLevel()
character = charChoice()
playGame(difficulty, character)


