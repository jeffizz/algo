#!/usr/bin/env python3

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        m, n = len(s), len(goal)
        if m != n:
            return False
        i = 0
        while i < m:
            if s[i] == goal[0]:
                p, q = i, 0
                while s[p%m] == goal[q]:
                    if q < m - 1:
                        p, q = p + 1, q + 1
                    else:
                        return True
            i += 1
        return False

    def rotateString2(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and s in (goal + goal)



print(Solution().rotateString('gcmbf', 'fgcmb'))
