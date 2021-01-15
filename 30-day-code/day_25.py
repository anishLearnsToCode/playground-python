def is_prime(number: int) -> bool:
    if number is 1:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


test_cases = int(input())
for _ in range(test_cases):
    number = int(input())
    print('Prime' if is_prime(number) else 'Not prime')
