#!/usr/bin/env python3

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j, m, n = 0, 0, len(s), len(t)
        while i < m and j <n:
            while j < n:
                if t[j] == s[i]:
                    i += 1
                    j += 1
                    break;
                j += 1
        return i >= m

s = 'abc'
t = 'ahbgdc'
print(Solution().isSubsequence(s, t))
