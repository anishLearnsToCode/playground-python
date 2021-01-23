# Normal Distribution I

from math import erf, sqrt


def phi(x, mu=0, sigma=1):
    'Cumulative distribution function for the normal distribution'
    return (1 + erf((x - mu) / (sigma * sqrt(2)))) / 2


mu, sigma = map(int, input().split())
b = float(input())
result = phi(b, mu, sigma)
print(f'{result:.3f}')

a, b = map(int, input().split())
result = phi(b, mu, sigma) - phi(a, mu, sigma)
print(f'{result:.3f}')
