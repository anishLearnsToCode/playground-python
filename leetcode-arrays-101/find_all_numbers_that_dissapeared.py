from typing import List


class Solution:
    def markUsed(self, array: List[int], index: int) -> None:
        if array[index] == 0:
            return
        value = array[index]
        array[index] = 0
        self.markUsed(array, value - 1)

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for element in nums:
            if element != 0:
                self.markUsed(nums, element - 1)
        result = []
        for index, element in enumerate(nums):
            if element != 0:
                result.append(index + 1)
        return result
