num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operation_type = input("Choose the operation (+, -, *, /): ")

match operation_type:
    case _ if operation_type == "+":
        print("Result is: ", num1 + num2)
    case _ if operation_type == "-":
        print ("Result is: ", num1 - num2)
    case _ if operation_type == "*":
        print ("Result is : ", num1 * num2)
    case _ if operation_type == "/":
        print ("Result is: ", num1/num2)

 