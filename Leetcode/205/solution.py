#!/usr/bin/env python3

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds, dt = {}, {}
        for i,c in enumerate(s):
            if c not in ds:
                ds[c] = t[i]
            else:
                if ds[c] != t[i]:
                    return False
            if t[i] not in dt:
                dt[t[i]] = c
            else:
                if dt[t[i]] != c:
                    return False
        return True

s = 'paper'
t = 'title'
print(Solution().isIsomorphic(s, t))


s = 'badc'
t = 'baba'
print(Solution().isIsomorphic(s, t))

s = 'bad'
t = 'bcc'
print(Solution().isIsomorphic(s, t))
