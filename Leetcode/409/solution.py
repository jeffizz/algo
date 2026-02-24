#!/usr/bin/env python3

from collections import defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for c in s:
            d[c] += 1

        odd,even = 0, 0
        for v in d.values():
            if v % 2 == 0:
                even += v
            else:
                odd += v - 1

        if odd > 0 or len(s) - even > 0:
            return even + odd + 1
        return even + odd

s = 'aaabbccc'
print(Solution().longestPalindrome(s))
