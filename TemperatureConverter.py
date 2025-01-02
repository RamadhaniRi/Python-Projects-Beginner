#TemperatureConverter

temp = float(input("Input the number: "))
unit = input("Input type of temperature (C, F, K, R): ")
unit = unit.upper()

if unit == "C":
    F = (temp * 9 / 5) + 32
    R = temp * 4 / 5
    K = temp + 273.15
    print(f"Fahrenheit value is {F:.2f}")
    print(f"Reamur value is {R:.2f}")
    print(f"Kelvin value is {K:.2f}")

elif unit == "F":
    C = (temp - 32) / 1.8
    R = ((temp - 32) / 1.8) * 4 / 5
    K = ((temp - 32) / 1.8) + 273.15
    print(f"Celcius value is {C:.2f}")
    print(f"Reamur value is {R:.2f}")
    print(f"Kelvin value is {K:.2f}")

elif unit == "R":
    C = temp * 5 / 4
    F = (temp * 9 / 4) + 32
    K = (temp * 5 / 4) + 273.15
    print(f"Celcius value is {C:.2f}")
    print(f"Fahrenheit value is {F:.2f}")
    print(f"Kelvin value is {K:.2f}")

elif unit == "K":
    C = temp - 273.15
    F = ((temp - 273.15) * 9 / 5) + 32
    R = ((temp - 273.15) * 4 / 5)
    print(f"Celcius value is {C:.2f}")
    print(f"Fahrenheit value is {F:.2f}")
    print(f"Reamur value is {R:.2f}")
else:
    print("input is invalid. Please enter a valid unit (C, F, K, R).")
