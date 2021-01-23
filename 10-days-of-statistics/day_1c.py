import math
from typing import List


def std(data: List[int]) -> float:
    mu = sum(data) / len(data)
    var = sum((element - mu) ** 2 for element in data) / len(data)
    return math.sqrt(var)


n = int(input())
X = list(map(int, input().split()))
sigma = std(X)
print(f'P{sigma:.1f}')
