#!/usr/bin/env python3

from typing import List

# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

# m = 1
# n = 0
# nums1 = [1]
# nums2 = []

# m = 0
# n = 1
# nums1 = [0]
# nums2 = [1]

# m = 4
# n = 2
# nums1 = [6,6,6,8,0,0]
# nums2 = [2,9]

# m = 2
# n = 4
# nums1 = [3,8,0,0,0,0]
# nums2 = [2,4,4,9]

m = 3
n = 3
nums1 = [1,2,3,0,0,0]
nums2 = [4,5,6]

# Wrong Direction
# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         i,j,k = 0,0,0
#         for i in range(m + n):
#             if i >= m:
#                 if k <= j:
#                     if j >= n or nums2[j] > nums2[k]:
#                         nums1[i] = nums2[k]
#                         k = n
#                         continue;
#                 if j < n:
#                     nums1[i] = nums2[j]
#                     if j == k:
#                         k = n
#                     j += 1
#                     continue;
#             if k < j: # --
#                 if nums1[i] >= nums2[k]:
#                     nums1[i], nums2[k] = nums2[k], nums1[i]
#                     continue;
#             if j < n:
#                 if nums1[i] > nums2[j]:
#                     nums1[i], nums2[j] = nums2[j], nums1[i]
#                     j += 1
#                     continue;
#

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


Solution().merge(nums1, m, nums2, n);
print(nums1)
