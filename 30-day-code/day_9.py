def factorial(n: int) -> int:
    return 1 if n is 0 else n * factorial(n - 1)


n = int(input())
print(factorial(n))
