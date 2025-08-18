def calculate_discount(price, discount_percent):
    
    if discount_percent >=20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

print(calculate_discount(200, 30))
print(calculate_discount(200, 15))    
    