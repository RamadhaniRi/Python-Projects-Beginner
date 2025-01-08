def find_minimum(numbers):
    minimum = numbers[0]
    for i in numbers:
        if i < minimum:
            minimum = i
        return minimum

print(find_minimum([6, 4, 3, 8, 9]))
