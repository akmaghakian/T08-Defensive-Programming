import os.path

def calculator():
    #Firstly we ask the user to enter two numbers and an operator.
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    operator = input("Enter the operation you wish to make (+, -, *, /): ")

    # Secondly we convert the input into numerical values.
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Thirdly we perform a calculation based on the operator.
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator. Please enter a valid operator.")
        return

    # Fourthly we print the result and write the equation in a file.
    print("Result: ", result)
    with open("equations.txt", "a") as f:
        f.write(str(num1) + " " + operator + " " + str(num2) + " = " + str(result) + "\n")

def calculator_file():
    #Fifthly, ask the user for a filename.
    filename = input("Enter the filename: ")
    
    # Sixthly we check if file exists
    while not os.path.exists(filename):
        print("File does not exist.")
        filename = input("Enter the filename: ")

    # Seventhly we read file and calculate results.
    with open(filename, "r") as f:
        equations = f.readlines()
        for eq in equations:
            parts = eq.split()
            num1 = float(parts[0])
            num2 = float(parts[2])
            operator = parts[1]
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Cannot divide by zero.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator in equation: ", eq)
                continue
            print(eq.strip(), "= ", result)

# Eighthly we set uo a main program loop to allow the user to exit the program or start the operations again.
while True:
    choice = input("Please enter 'c' for calculator, 'f' to calculate and read from file, or 'q' to quit: ")
    if choice == "c":
        calculator()
    elif choice == "f":
        calculator_file()
    elif choice == "q":
        break
    else:
        print("Invalid choice. Please enter 'c', 'f', or 'q'.")