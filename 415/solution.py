#!/usr/bin/env python3

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1)-1, len(num2)-1
        s = ""
        t = 0
        while m>=0 or n >= 0:
            x1 = int(num1[m]) if m >= 0 else 0
            x2 = int(num2[n]) if n >= 0 else 0
            c = t + x1 + x2
            t = (c - c % 10) // 10
            s = str(c % 10) + s
            m, n = m - 1, n - 1
        if t > 0:
            s = str(t) + s
        return s

print(Solution().addStrings("123", "11"))
