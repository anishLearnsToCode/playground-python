from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) is 0: return 0
        finalLength = 1
        index, current = 1, nums[0]
        while index < len(nums):
            if nums[index] != current:
                nums[finalLength] = nums[index]
                finalLength += 1
                current = nums[index]
            index += 1
        return finalLength
