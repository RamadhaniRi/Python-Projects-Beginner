#WeightConverter

weight = float(input("Enter your weight: "))
unit = input("Kg or Lbs (K or L)!")

if unit == "K":
    weight = weight * 3
    print(f"your weight is {weight} lbs")
elif unit == "L":
    weight = weight / 3
    print(f"your weight is {weight} kg")
else:
    print(f"{unit} is invalid input")

