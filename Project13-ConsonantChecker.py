def is_consonant(char): 
    vowels = ["a", "i", "u", "e", "o"]
    if char.isalpha() and char.lower() not in vowels:  # Pastikan huruf dan bukan vokal
        return True
    return False  # Jika vokal atau bukan huruf, kembalikan False

print(is_consonant("b"))  # Output: True
print(is_consonant("a"))  # Output: False
print(is_consonant("1"))  # Output: False
print(is_consonant("$"))  # Output: False
