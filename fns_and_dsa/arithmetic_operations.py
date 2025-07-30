
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
    elif operation == "divide":
        if num2 == 0:
            return "The result is not defined (division by zero)"
        else:
            return num1 / num2
    else:
        print ("Input is incorrect.")

result = perform_operation(num1, num2, operation)
print("Result: ", result)