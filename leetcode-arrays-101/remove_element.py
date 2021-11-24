from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        finalLength = 0
        for element in nums:
            if element is not val:
                nums[finalLength] = element
                finalLength += 1
        return finalLength
