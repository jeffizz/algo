#!/usr/bin/env python3

from typing import List

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = len(nums)
        j,k = 1,0
        while j < m:
            if nums[k] == nums[j]:
                j += 1
            else:
                k += 1
                nums[k] = nums[j]
        return k + 1


Solution().removeDuplicates(nums);
print(nums)
