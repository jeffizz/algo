#!/usr/bin/env python3

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            elif nums[m] > target:
                j = m - 1
            else:
                return m
        return -1

print(Solution().search([5], 5))
print(Solution().search([2,5], 2))
print(Solution().search([2,5], 5))
print(Solution().search([-1,0,3,5,9,12], 9))
print(Solution().search([-1,0,3,5,9,12], 2))
print(Solution().search([-1,0,3,5,9,12], 24))
