#!/usr/bin/env python3

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        sum, i = 0, 0
        while i < len(s)-1:
            if d[s[i]] < d[s[i+1]]:
                sum += d[s[i+1]] - d[s[i]]
                i += 1
            else:
                sum += d[s[i]]
            i += 1
        sum += (d[s[i]] if i == (len(s) -1) else 0)
        return sum


    def romanToInt2(self, s: str) -> int:
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        sum = 0
        size = len(s)
        for i in range(size-1):
            if d[s[i]] < d[s[i+1]]:
                sum -= d[s[i]]
            else:
                sum += d[s[i]]
        sum += d[s[size-1]]
        return sum


s = 'MCMXCIV'
result = Solution().romanToInt(s)
print(result)

