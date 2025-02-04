#!/usr/bin/env python3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            d[c] = d.setdefault(c, 0) + 1
        for x in t:
            if x not in d:
                return False
            d[x] -= 1
            if not d[x]:
                del d[x]
        return not len(d)


s = 'anagram'
t = 'nagaram'
print(Solution().isAnagram(s, t))

s = 'anagram'
t = 'ngaram'
print(Solution().isAnagram(s, t))

s = 'anagram'
t = 'nagaramt'
print(Solution().isAnagram(s, t))

