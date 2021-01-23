# Pearson Correlation Coefficient
from typing import List
import math


def descriptive_stats(data: List[float]) -> tuple:
    mu = sum(data) / len(data)
    var = sum(map(lambda x: (x - mu) ** 2, data)) / len(data)
    std = math.sqrt(var)
    return mu, std


def cov(X: List[float], Y: List[float], mu_x: float, mu_y: float) -> float:
    return sum(map(lambda x: (x[0] - mu_x) * (x[1] - mu_y), zip(X, Y)))


n = int(input())
X = list(map(float, input().split()))
Y = list(map(float, input().split()))

mu_x, std_x = descriptive_stats(X)
mu_y, std_y = descriptive_stats(Y)
cov_XY = cov(X, Y, mu_x, mu_y)
r = cov_XY / (n * std_x * std_y)
print(round(r, 3))
