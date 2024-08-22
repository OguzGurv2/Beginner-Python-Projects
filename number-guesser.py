# Importing random and time modules for:
# randomizing numbers and to delay responds.

import random
import time

# Intro of the game when the file executed.
print("This is a number guessing game!")

# Main game function that starts the game.
def main():

    # randrange function randomizes an integer between to numbers.
    guess_number = random.randrange(1, 5)
    time.sleep(1)
    print("Guess from 1-5.")

    # Checks user input with an external function.
    user_number = check_input(input())

    # Checks if user's input equals to the randomized number 
    if guess_number == user_number :
        print("You won!")
        time.sleep(1)
        # Asks for a new game and restarts the game according to the input.
        print("Do you want to replay? (y/n)")
        restart_game(input())
    else:
        # If user lost shows the computer's number.
        print("Try again!" + "\nThe number was: " + str(guess_number))
        time.sleep(1)
        print("Do you want to replay? (y/n)")
        restart_game(input())


def check_input(input_string):
    # Checks if the input is an integer with .isdigit() function.
    if input_string.isdigit(): 
        # Checks the number if it's between 1 to 5.
        if int(input_string) > 0 and int(input_string) < 6:
            # Returns the input value as an integer to the variable
            return int(input_string)
        else:
            # Gives error as an output then recalls the function with new input.
            print("Error: Number needs to be between 1 to 5.")
            check_input(input())
    else:
        # Gives error as an output then recalls the function with new input.
        print("Error: Please type an integer!")
        check_input(input())

# Restarting function to give errors if necessary and runs the main function if needed.
def restart_game(param):
    if param == "y":
        main()
    elif param == "n":
        quit()
    else:
        print("Error: Please type `y` for yes or `n` for no.")
        restart_game(input())

main()