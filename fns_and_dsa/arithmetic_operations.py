
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

def perform_operation(num1, num2, operation):

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide" :
        print("The result is: ", division)
    elif operation == "divide" and num2 == 0:
        print("The result is not defined")
    else:
        print ("Input is incorrect.")

perform_operation()