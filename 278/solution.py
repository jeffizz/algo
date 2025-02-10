#!/usr/bin/env python3

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i, j, b = 1, n, 0
        while i <= j :
            m = (i + j) // 2
            if isBadVersion(m):
                b = m
                j = m - 1
            else:
                i = m + 1
        return b
