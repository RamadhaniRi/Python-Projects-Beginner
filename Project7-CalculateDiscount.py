def calculate_discount(price, discount):
    final_price = price - (price * discount / 100)
    return final_price

print(calculate_discount(100, 10))
