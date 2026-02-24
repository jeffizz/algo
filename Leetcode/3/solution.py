#!/usr/bin/env python3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if  n <= 1:
            return n
        i,j,m = 0,0,0
        while j < n - 1:
            k = i
            j += 1
            while k < j:
                if s[k] == s[j]:
                    i = k + 1
                    break
                k += 1
            if m < (j - i + 1):
                m = j - i + 1
        return m






print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("abcabef"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("dvdf"))
