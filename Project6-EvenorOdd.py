#EvenorOdd

number = int(input("input your number: "))

if number % 2 == 0:
    print("number is Even")
else:
    print("number is Odd")


#diatas versi asli, dibawah versi yang lebih bagus


def EvenorOdd(number) :
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

user_input = int(input("input your number: "))
print(EvenorOdd(user_input))
