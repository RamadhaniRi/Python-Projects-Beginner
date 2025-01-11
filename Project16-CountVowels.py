def count_vowels(text):
    vowel = ["a", "i", "u", "e", "o"]
    count = 0
    for i in text.lower():  # Menggunakan .lower() agar periksa huruf besar dan kecil
        if i in vowel:
            count += 1
    return count

print(count_vowels("Hello World"))  # Output: 5
