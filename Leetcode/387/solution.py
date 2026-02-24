#!/usr/bin/env python3

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            if c not in d:
                d[c] = i
            else:
                d[c] -= i
        min = -1
        for i in d.values():
            if i >= 0:
                if min == -1:
                    min = i
                else:
                    min = i if i <= min else min
        return min

    def firstUniqChar2(self, s: str) -> int:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for i, c in enumerate(s):
            if dic[c]: return i
        return -1

s = 'loveleetcode'
print(Solution().firstUniqChar(s))
