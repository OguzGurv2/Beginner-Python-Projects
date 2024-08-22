import random
import time

print("This is a number guessing game!")
def start_game():
    guess_number = random.randrange(1, 5)
    time.sleep(1)
    print("Guess from 1-5.")
    user_number = check_input(input())

    if guess_number == user_number :
        print("You won!")
        time.sleep(1)
        print("Do you want to replay? (y/n)")
        replay = input()
    else:
        print("The number was: " + str(guess_number))
        time.sleep(1)
        print("Try again!")
        time.sleep(1)
        print("Do you want to replay? (y/n)")
        replay = input()
    
    if replay == "y":
        start_game()
    else:
        quit()

def check_input(input_string):
    if input_string.isdigit(): 
        if int(input_string) > 0 and int(input_string) < 6:
            return int(input_string)
        else:
            print("Error: Number needs to be between 1 to 5.")
            check_input(input())
    else:
        print("Error: Please type a number!")
        check_input(input())

start_game()