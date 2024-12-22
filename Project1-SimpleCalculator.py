#PythonProject
#SimpleCalculator

operator = input("Input the operator (+ - * /): ")
num1 = float(input("input the 1st number: "))
num2 = float(input("input the 2nd number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else:
    print(f"{operator} is not valid operator")

print(result)
