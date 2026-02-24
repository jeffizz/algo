#!/usr/bin/env python3

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r,f = [],{}
        i = 0
        n = len(nums)
        while i < n - 2:
            j = i + 1
            while j < n - 1:
                k = j + 1
                x = -(nums[i] + nums[j])
                while k < n:
                    if nums[k] == x:
                        t = (nums[i], nums[j], nums[k])
                        if t not in f:
                            f[t] = 1
                            r.append(list(t))
                        break
                    elif nums[k] > x:
                        break
                    k += 1
                j += 1
            i += 1
        return r




print(Solution().threeSum([-1,0,1,2,-1,-4]))
