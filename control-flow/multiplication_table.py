number = int(input("Enter a number to see its multiplication table: "))
# factors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for factor in range(1, 11):
    result = number * factor
    print(f"{number} * {factor} = {result}")