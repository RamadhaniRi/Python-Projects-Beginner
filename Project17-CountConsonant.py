def count_consonant(text):
    
    vowel = ["a", "i", "u", "e", "o"]
    count = 0
    for i in text:
        if i != ' ' and i not in vowel:
            count += 1
    return count
    

print(count_consonant("World")) #output = 4
