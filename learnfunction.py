# def say_hello():
#     return "Hello, World"

# print(say_hello())

# def greet(name):
#     return name

# print(greet("Denny"))

# def add_numbers(x, y):
#     z = x + y
#     return z

# print(add_numbers(5, 4))

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
    
# print(is_even(5))

# def get_max(num1, num2):
#     max_num = max(num1, num2)
#     return max_num

# print(get_max(10, 2))


def is_palindrome(word):
    reverse = word[::-1]
    if word == reverse:
        return True
    else:
        return False

print(is_palindrome("buku"))
print(is_palindrome("madam"))

def mltply(a, b): 
    z = a * b
    return z

print(mltply(5, 4))
