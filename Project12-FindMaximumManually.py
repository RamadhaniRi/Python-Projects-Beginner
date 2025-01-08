def find_maximum(numbers):
    maximum = numbers[0]
    for i in numbers:
        if i > maximum:
            maximum = i
    return maximum

print(find_maximum([6, 9, 3, 8, 15]))
