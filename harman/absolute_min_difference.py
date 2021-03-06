from typing import List


def binary_search(array: List[int], x: int) -> int:
    left, right = 0, len(array) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if array[middle] == x: return middle
        elif array[middle] < x: left = middle + 1
        else: right = middle - 1
    return left


def values_absolute_min_difference(array_1: List[int], array_2: List[int]) -> List[int]:
    array_1, array_2 = (array_2, array_1) if len(array_1) < len(array_2) else (array_1, array_2)
    array_2.sort()
    result = []
    min_abs_diff = float('inf')

    for number in array_1:
        position = binary_search(array_2, number)
        p1, p2 = position - 1, position
        if (p1 >= 0) and (abs(number - array_2[p1]) < min_abs_diff):
            min_abs_diff = abs(number - array_2[p1])
            result = [number, array_2[p1]]
        if (p2 < len(array_2)) and (abs(number - array_2[p2]) < min_abs_diff):
            min_abs_diff = abs(number - array_2[p2])
            result = [number, array_2[p2]]
        if (position < len(array_2)) and (array_2[position] == number):
            return [number, number]

    return result


l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

print(values_absolute_min_difference(l1, l2))
