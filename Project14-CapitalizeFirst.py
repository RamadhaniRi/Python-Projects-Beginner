def capitalize_first(text):
    words = text.split()  # Pisahkan string menjadi daftar kata
    capitalized_words = [word.capitalize() for word in words]  # Kapitalisasi setiap kata
    return ' '.join(capitalized_words)  # Gabungkan kembali kata-kata dengan spasi

print(capitalize_first("selamat pagi denny"))  # Output: "Selamat Pagi Denny"
