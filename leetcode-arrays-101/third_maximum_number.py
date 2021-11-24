from typing import List


class Solution:
    def thirdMax(self, array: List[int]) -> int:
        if len(array) == 1: return array[0]
        if len(array) == 2: return max(array[0], array[1])
        infinity = float('inf')
        first, second, third = array[0], -infinity, -infinity
        index = 1
        while index < len(array):
            if array[index] > first:
                third = second
                second = first
                first = array[index]
            elif second < array[index] < first:
                third = second
                second = array[index]
            elif third < array[index] < second:
                third = array[index]
            index += 1
        return first if third == -infinity else third
