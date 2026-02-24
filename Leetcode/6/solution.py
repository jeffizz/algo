#!/usr/bin/env python3

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        r = [""] * numRows
        i,j,x = 0,0,0
        d = numRows - 1
        while i < len(s) - 1:
            i += 1
            if x % 2 == 0:
                j += 1
                r[j] += s[i]
            else:
                j -= 1
                r[j] += s[i]
            if i % d == 0: x += 1
        return s[0] + "".join(r)

print(Solution().convert("PAYPALISHIRING", 3))
print(Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
print(Solution().convert("PAYPALISHIRING", 4))
print(Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
print(Solution().convert("PAYPALISHIRING", 5))
print(Solution().convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN")
