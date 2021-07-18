def calculate_discount(amount: int) -> int:
    odd_digits, even_digits = 0, 0
    for digit in str(amount):
        if int(digit) % 2 == 0:
            even_digits += int(digit)
        else:
            odd_digits += int(digit)
    return odd_digits * even_digits


amount = int(input())
print(calculate_discount(amount))
