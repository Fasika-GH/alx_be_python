def perform_operation(num1, num2, operation):

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
    elif num2 == 0 and operation == "divide":
        print("The result is not defined")
    else:
        print ("Input is incorrect.")

perform_operation()