
weight = float(input("Enter your weight: "))
unit = input("kilograms or pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    unit = "lbs"
    print(f"Your weight in pounds is {round(weight, 1)} {unit}")

elif unit == "L":
    weight = weight / 2.205
    unit = "kgs"
    print(f"Your weight in pounds is {round(weight, 1)} {unit}")
else:
    print(f"{unit} is not a valid weight")

