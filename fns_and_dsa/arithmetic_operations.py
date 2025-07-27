def perform_operation():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1/num2

    if operation == "add":
        print("The result is: ", addition)
    elif operation == "subtract":
        print("The result is: " + subtraction)
    elif operation == "multiply":
        print("The result is: ", multiplication)
    elif operation == "divide" :
        print("The result is: ", division)
    elif operation == "divide" and num2 == 0:
        print("The result is not defined")
    else:
        print ("Input is incorrect.")

perform_operation()