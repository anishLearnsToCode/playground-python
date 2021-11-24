from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        finalLength = 0
        index = 0
        while index < len(nums):
            if nums[index] != 0:
                nums[finalLength] = nums[index]
                finalLength += 1
            index += 1
        while finalLength < len(nums):
            nums[finalLength] = 0
            finalLength += 1
