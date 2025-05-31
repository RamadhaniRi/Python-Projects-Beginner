year = int(input("Input the year: "))

if year % 400 == 0:
    print("Special Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("Ordinary Leap Year")
else:
    print("Ordinary Year")
    