from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        differences = 0
        for e, h in zip(expected, heights):
            if e != h:
                differences += 1
        return differences
