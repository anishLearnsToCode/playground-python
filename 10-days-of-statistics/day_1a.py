from math import ceil
from typing import List


def median(numbers: List[int]) -> float:
    n = len(numbers)
    result = numbers[n // 2]
    if len(numbers) % 2 == 0:
        result = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
    return result


n = int(input())
data = list(map(int, input().split()))
data.sort()
left = data[0: n // 2]
right = data[ceil(n / 2) :]

print(int(median(left)))
print(int(median(data)))
print(int(median(right)))
