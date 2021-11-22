from typing import List


class Solution:
    def sortedSquares(self, array: List[int]) -> List[int]:
        result = [0] * len(array)
        left, right, k = 0, len(array) - 1, len(array) - 1
        while left <= right:
            if abs(array[left]) > abs(array[right]):
                result[k] = array[left] ** 2
                left += 1
            else:
                result[k] = array[right] ** 2
                right -= 1
            k -= 1
        return result
