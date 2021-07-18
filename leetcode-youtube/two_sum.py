from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappings = {}
        for index, value in enumerate(nums):
            mappings[value] = index

        for index, value in enumerate(nums):
            required = target - value
            if required in mappings and mappings[required] != index:
                return [index, mappings[required]]
