#!/usr/bin/env python3

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

haystack = "leetcode"
needle = "leeto"
print(Solution().strStr(haystack, needle))
