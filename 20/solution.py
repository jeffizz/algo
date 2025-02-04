#!/usr/bin/env python3

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in {'(', '[', '{'}:
                stack.append(c)
            else:
                if stack and d[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return not bool(stack)



s = '(){}}{'
print(Solution().isValid(s))
s = ']'
print(Solution().isValid(s))
