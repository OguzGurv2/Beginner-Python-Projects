import math
import time

print("Welcome to simple calculator!")

def main ():
    
    # Gets the operation selection by input.
    time.sleep(1)
    print("Which operation do you want to do? \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Square Root \n6. Power of \n7. Quit")
    operation_selection = check_input(input(), True)

    # According to the variable operation() function is called with parametes.
    if operation_selection == 1:
        operation(operation_selection)
    elif operation_selection == 2:
        operation(operation_selection)
    elif operation_selection == 3:
        operation(operation_selection)
    elif operation_selection == 4:
        operation(operation_selection)
    elif operation_selection == 5:
        operation(operation_selection)
    elif operation_selection == 6:
        operation(operation_selection)
    else:
        quit()

def operation(param):

    operation_list = ["+", "-", "*", "/", "√", "^"]
    
    # Checking the param to process the operation
    time.sleep(1)
    if param == 5:
        # Square root operation only needs one input
        print("Enter a number!")
        string_a = input()
        a = check_input(string_a, False)
        result = math.sqrt(a)
        time.sleep(1)
        print(f"{operation_list[param - 1]}{string_a}  =  {str(result)}")
    else:
        # Other operations needs at least two input
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
        elif param == 6:
            result = math.pow(a, b)
        # Does the operation according to the operation parameter.

        # Output with correct operation sign.
        time.sleep(1)
        print(f"{string_a} {operation_list[param - 1]} {string_b}  =  {str(result)}")

    time.sleep(1)
    print("Do you want to do another operation? (y/n)")
    restart_calculator(input())

def check_input(input_string, is_selection):
    # Checks if the input is an integer with .isdigit() function.
    while True:
        if input_string.isdigit(): 
            if is_selection:
                # Checks the number if it's between 1 to 5.
                if int(input_string) > 0 and int(input_string) < 6:
                    # Returns the input value as an integer to the variable
                    return int(input_string)
                else:
                    # Gives error as an output then recalls the function with new input.
                    print("Error: Operation not found.")
            else:
                return int(input_string)
        else:
            # Gives error as an output then recalls the function with new input.
            print("Error: Please type an integer!")

# Restarting function to give errors if necessary and runs the main function if needed.
def restart_calculator(param):
    if param.lower() == "y":
        main()
    elif param.lower() == "n":
        quit()
    else:
        print("Error: Please type `y` for yes or `n` for no.")
        restart_calculator(input())

main()