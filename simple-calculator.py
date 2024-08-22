import math
import time

print("Welcome to simple calculator!")

def main ():
    
    time.sleep(1)
    print("Which operation do you want to do? \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Quit")
    operation_selection = check_input(input(), True)

    if operation_selection == 1:
        operation(operation_selection)
    elif operation_selection == 2:
        operation(operation_selection)
    elif operation_selection == 3:
        operation(operation_selection)
    elif operation_selection == 4:
        operation(operation_selection)
    else:
        quit()

def operation(param):

    operation_list = ["+", "-", "*", "/"]
    
    time.sleep(1)
    print("First number:")
    string_a = input()
    a = check_input(string_a, False)

    print("Second number:")
    string_b = input()
    b = check_input(string_b, False)

    if param == 1:  
        result = a + b
    elif param == 2: 
        result = a - b
    elif param == 3:  
        result = a * b
    elif param == 4:  
        if b != 0:
            result = a / b
        else:
            print("Cannot divide by zero.")
            return

    time.sleep(1)
    print(f"{string_a} {operation_list[param - 1]} {string_b}  =  {str(result)}")

    time.sleep(1)
    print("Do you want to do another operation? (y/n)")
    restart_calculator(input())

def check_input(input_string, is_selection):
    # Checks if the input is an integer with .isdigit() function.
    if input_string.isdigit(): 
        if is_selection:
            # Checks the number if it's between 1 to 5.
            if int(input_string) > 0 and int(input_string) < 6:
                # Returns the input value as an integer to the variable
                return int(input_string)
            else:
                # Gives error as an output then recalls the function with new input.
                print("Error: Operation not found.")
                check_input(input(), is_selection)
        else:
            return int(input_string)
    else:
        # Gives error as an output then recalls the function with new input.
        print("Error: Please type an integer!")
        check_input(input(), is_selection)

# Restarting function to give errors if necessary and runs the main function if needed.
def restart_calculator(param):
    if param == "y":
        main()
    elif param == "n":
        quit()
    else:
        print("Error: Please type `y` for yes or `n` for no.")
        restart_calculator(input())

main()