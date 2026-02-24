#!/usr/bin/env python3

from typing import List

class Solution:
    # O(n * log(n))
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, m = 0, 1
        while i < len(numbers) - 1:
            t = target - numbers[i]
            j = i + 1
            k = len(numbers) - 1
            while j <= k:
                m = (j + k) // 2
                if numbers[m] > t:
                    k = m - 1
                elif numbers[m] < t:
                    j = m + 1
                else: return [i+1, m+1]
            i += 1
        return [i+1, m+1]

    # O(n)
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else: return [i+1, j+1]
        return [i+1, j+1]

print(Solution().twoSum2([2,7,11,15], 9))
print(Solution().twoSum2([2,3,4], 6))
print(Solution().twoSum2([-1, 0], -1))
