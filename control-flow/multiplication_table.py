number = int(input("Enter a number to see its multiplication table: "))
factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in factors:
    result = number * item
    print(number, " * ", item, " = ", result)