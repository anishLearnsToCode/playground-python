from typing import List


def is_increasing(array: List[float]) -> bool:
    prev = array[0]
    for i in range(1, len(array)):
        if array[i] < prev:
            return False
        prev = array[i]
    return True


def is_decreasing(array: List[float]) -> bool:
    prev = array[0]
    for i in range(1, len(array)):
        if array[i] > prev:
            return False
        prev = array[i]
    return True


numbers = list(map(float, input().split()))
print(is_decreasing(numbers) or is_increasing(numbers))
