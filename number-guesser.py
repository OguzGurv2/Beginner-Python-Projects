import random
import time

# Intro of the game when the file is executed.
print("This is a number guessing game!")

# Main game function that starts the game.
def main():
    time.sleep(1)
    print("From zero to which number do you want to guess?")
    range_value = check_input(input(), is_range=True)

    # Randomly select a number between 0 and range_value
    time.sleep(1)
    guess_number = random.randrange(0, range_value + 1)
    print(f"Guess from 0 to {range_value}.")

    # Get user's guess and validate it
    user_number = check_input(input(), is_range=False, range_value=range_value)

    # Check if the user's guess matches the random number
    if guess_number == user_number:
        print("You won!")
    else:
        print(f"Try again! The number was: {guess_number}")

    time.sleep(1)
    print("Do you want to replay? (y/n)")
    restart_game(input())

# Function to check user input and validate it
def check_input(input_string, is_range, range_value=None):
    # While loop for better handling the process
    while True: 
        # Checks if the input is a digit
        if input_string.isdigit(): 
            num = int(input_string)
            # If we are setting the range
            if is_range: 
                if num > 0:
                    return num
                else:
                    print("Error: The range needs to be more than 0.")
            # If the input is for guessing
            else: 
                if 0 <= num <= range_value:
                    return num
                else:
                    print(f"Error: The number needs to be between 0 and {range_value}.")
        else:
            print("Error: Please type an integer!")

        # If input is invalid, ask for input again
        input_string = input()

# Function to restart or quit the game based on user's input
def restart_game(param):
    if param.lower() == "y":
        main()
    elif param.lower() == "n":
        quit()
    else:
        print("Error: Please type `y` for yes or `n` for no.")
        restart_game(input())

# Start the game
main()