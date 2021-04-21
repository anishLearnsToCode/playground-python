from typing import List


def linear_search(numbers: List[int], element: int) -> int:
    for index, number in enumerate(numbers):
        if number == element:
            return index
    return -1


def binary_search(numbers: List[int], element: int) -> int:
    left, right, middle = 0, len(numbers), 0
    while left <= right:
        middle = left + (right - left) // 2
        if numbers[middle] == element: return middle
        elif numbers[middle] > element: right = middle - 1
        else: right = middle + 1
    return -1


array = list(map(int, input().split()))
x = int(input())
print(binary_search(array, x))
