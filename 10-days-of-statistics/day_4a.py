# Binomial Distribution I
from math import factorial


def c(r: int, n: int) -> int:
    return factorial(n) // (factorial(n - r) * factorial(r))


b, g = map(float, input().split())
p_b = b / (b + g)
p_g = g / (b + g)
result = 0

for i in range(3, 7):
    result += c(i, 6) * (p_b ** i) * (p_g ** (6 - i))

print(f'{result:.3f}')
