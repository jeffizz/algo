#!/usr/bin/env python3

from typing import List

nums = [2,3,1,2,2,4,9,2,6,8,2,2,0,7,2,5,2,6,2,2,2]
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        m = len(nums)
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
            if d[num] > m/2:
                return num
        return 0



result = Solution().majorityElement(nums)
print(result)


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

result = Solution2().majorityElement(nums)
print(result)
