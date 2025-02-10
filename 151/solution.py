#!/usr/bin/env python3

class Solution:
    def reverseWords(self, s: str) -> str:
        t = r = ""
        for c in s:
            if c == ' ' and not t: continue
            elif c == ' ' and t:
                r = " " + t + r
                t = ""
            else: t += c
        return t + r if t else r[1:]

    def reverseWords2(self, s: str) -> str:
        return ' '.join(s.strip().split()[::-1])



print(Solution().reverseWords2("  aaa   asds   "))
