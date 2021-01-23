# Normal Distribution II

from math import erf, sqrt


def phi(x, mu=0, sigma=1):
    'Cumulative distribution function for the normal distribution'
    return (1 + erf((x - mu) / (sigma * sqrt(2)))) / 2


mu, sigma = 70, 10

# What percentage scored higher than 80 in the exam?
result = (1 - phi(80, mu, sigma)) * 100
print(f'{result:.2f}')

# Percentage with grade >= 60
result = (1 - phi(60, mu, sigma)) * 100
print(f'{result:.2f}')

# Percentage failed the test (grade < 60)
result = phi(60, mu, sigma) * 100
print(f'{result:.2f}')
