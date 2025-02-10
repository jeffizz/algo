#!/usr/bin/env python3

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Binary Search not working, there are situations that ...
        # i, j = 0, len(nums) - 1
        # while i <= j:
        #     m = (i + j) // 2
        #     sl = abs(sum(nums[:m]))
        #     sr = abs(sum(nums[m+1:]))
        #     if sl > sr: j = m - 1
        #     elif sl < sr: i = m + 1
        #     else: return m
        # return -1
        left,right = 0, sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
        return -1


print(Solution().pivotIndex([1,7,3,6,5,6]))
print(Solution().pivotIndex([1,2,3]))
print(Solution().pivotIndex([2,1,-1]))
print(Solution().pivotIndex([-1,-1,-1,-1,-1,0]))
print(Solution().pivotIndex([-1,-1,-1,-1,0,1]))
# 二分不可解, 往左或者往右,都有可能达到平衡
print(Solution().pivotIndex([-1,-1,0,1,0,-1]))
