# Poisson Distribution I

from math import e, factorial


mu = float(input())
k = int(input())

result = (mu ** k) * (e ** -mu) / factorial(k)
print(f'{result:.3f}')
