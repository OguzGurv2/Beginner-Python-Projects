import math
import time

print("Welcome to simple calculator!")

def main ():
    
    # Gets the operation selection by input.
    time.sleep(1)
    print("Which operation do you want to do? \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Square Root \n6. Power of \n7. Quit")
    operation_selection = check_input(input(), True, False)

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
        a = check_input(string_a, False, False)
        result = math.sqrt(a)
        time.sleep(1)
        print(f"{operation_list[param - 1]}{string_a}  =  {str(result)}")
    else:
        # Other operations needs at least two input
        print("First number:")
        string_a = input()
        a = check_input(string_a, False, False)
        print("Second number:")
        string_b = input()
        if param == 4:  
            b = check_input(string_b, False, True)
            result = a / b
        else: 
            b = check_input(string_b, False, False)
            if param == 1:  
                result = a + b
            elif param == 2: 
                result = a - b
            elif param == 3:  
                result = a * b
            elif param == 6:
                result = math.pow(a, b)
        # Does the operation according to the operation parameter.

        # Output with correct operation sign.
        time.sleep(1)
        print(f"{a} {operation_list[param - 1]} {b}  =  {str(result)}")

    time.sleep(1)
    print("Do you want to do another operation? (y/n)")
    restart_calculator(input())

def check_input(input_string, is_selection, is_division):
    while True:
        if input_string.isdigit(): 
            if is_selection:
                # Checks the number if it's between 1 to 7.
                if 0 < int(input_string) and int(input_string) < 8:
                    # Returns the input value as an integer to the variable
                    return int(input_string)
                else:
                    print("Error: Operation not found. Please type a number between 1 and 7.")
                    input_string = input()  # Ask for new input
            elif is_division:
                if 0 == int(input_string):
                    print("Error: Cannot divide by zero.")
                    input_string = input()
                else:
                    return int(input_string)
            else:
                return int(input_string)
        else:
            print("Error: Please type an integer!")
            input_string = input()  # Ask for new input

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