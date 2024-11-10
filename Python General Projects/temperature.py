
unit = input("Is this temperature in Celcius or Fahrenheit? ")

temp = float(input("Enter temperature in Fahrenheit or Celcius: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"The temperature in Fahrenheit is {temp} °F")
elif unit == "F":
    pass

else:
    print(f"{unit} is not a valid unit of measurement")