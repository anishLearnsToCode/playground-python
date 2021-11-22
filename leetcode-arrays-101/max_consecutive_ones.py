from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, array: List[int]) -> int:
        result, current = 0, 0
        for element in array:
            if element is 1:
                current += 1
                result = max(result, current)
            else:
                current = 0
        return result
