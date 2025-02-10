#!/usr/bin/env python3

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m, t = 1, set()
        if len(s) <= 1: return len(s)
        for c in s:
            if c not in t: t.add(c)
            else:
                if len(t) > m:
                    m = len(t)
                t = set(c)
        return m if len(t) < m else len(t)





print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("abcabef"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("dvdf"))
