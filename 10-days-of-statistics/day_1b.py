from math import ceil
from typing import List


def median(data: List[int]) -> float:
    n = len(data)
    result = data[n // 2]
    if n % 2 == 0:
        result = (data[n // 2 - 1]+ data[n // 2]) / 2
    return result


n = int(input())
X = list(map(int, input().split()))
F = list(map(int, input().split()))

numbers = []
for index in range(n):
    for i in range(F[index]):
        numbers.append(X[index])

numbers.sort()
n = len(numbers)
left = numbers[: n // 2]
right = numbers[ceil(n / 2):]
quartile_1 = median(left)
quartile_3 = median(right)
inter_quartile_range = quartile_3 - quartile_1
print(f'{inter_quartile_range:.1f}')
