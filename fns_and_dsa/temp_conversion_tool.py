FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
temp_input = float(input("Enter the temperature to convert: "))
temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
fahrenheit = temp_input
celsius = temp_input

if temp_unit == "f":
    def convert_to_celsius(fahrenheit):
        converted_temp_celsius = (fahrenheit-32) * FAHRENHEIT_TO_CELSIUS_FACTOR
        print(converted_temp_celsius, "° C")
    convert_to_celsius(fahrenheit)

elif temp_unit == "c":
    def convert_to_fahrenheit(celsius):
        converted_temp_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
        print(converted_temp_fahrenheit, "° F")
    convert_to_fahrenheit(celsius)