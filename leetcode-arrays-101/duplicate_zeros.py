from typing import List


class Solution:
    def duplicateZeros(self, array: List[int]) -> None:
        removals, k, i = 0, len(array) - 1, 0
        while i < len(array) - removals:
            if array[i] is 0:
                if i == len(array) - removals - 1:
                    array[k] = 0
                    k -= 1
                removals += 1
            i += 1

        i = len(array) - removals - 1
        while i >= 0:
            if array[i] is 0:
                array[k], array[k - 1] = 0, 0
                k -= 1
            else:
                array[k] = array[i]
            k -= 1
            i -= 1
