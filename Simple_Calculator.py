WelMsg=("===========Welcome to Simple Calculator============")
print(WelMsg)  

while True:
    while True:
        try:
            operation = input("Choose an operation(+,-,*,/): ") #Get user's choice of operation
            if operation not in "+-*/":
                raise ValueError("Invalid operation. Please choose +, -, *, or /.")
            break  # Exit the inner loop if valid operation is entered
        except ValueError as e:
            print(e)  # Inform the user about the specific error provide more specific messages and guiding user towards valid input.

        
        # Get user's numbers with input validation
    while True:
        try:
            a = float(input("Enter the 1st Number: "))
            b = float(input("Enter the 2nd Number: "))
            break  # Exit the inner loop if valid numbers are entered
        except ValueError:
            print("Invalid input! Please enter only numbers (integers or decimals).")
    # Perform calculation based on choice
    if operation == "+":
        result = a + b
        print(f"Addition of {a} + {b} = {result}")
    elif operation == "-":
        result = a - b
        print(f"Subtraction of {a} - {b} = {result}")
    elif operation == "*":
        result = a * b
        print(f"Multiplication of {a} * {b} = {result}")
    elif operation == "/":
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = a / b
            print(f"Division of {a} / {b} = {result}")

    # Show Thank you message after successful calculation
    print("Thank you for using the Simple Calculator!")

    # Ask if user wants to continue (optional)
    choice = input("Do you want to perform another calculation? (y/n): ").lower()
    if choice != "y":
        break  # Exit the main loop if user chooses not to continue

        


