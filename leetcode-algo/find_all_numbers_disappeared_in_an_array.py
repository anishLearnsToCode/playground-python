from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for number in nums:
            if nums[number - 1] > 0:
                nums[number - 1] = -nums[number - 1]

        print(nums)

        result = []
        for index, number in enumerate(nums):
            if number > 0:
                result.append(index + 1)
        print(result)
        return result


sol = Solution()
sol.findDisappearedNumbers(nums=[4,3,2,7,8,2,3,1])
