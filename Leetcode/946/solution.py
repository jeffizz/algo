#!/usr/bin/env python3

from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, n = 0, len(popped)
        stack = []
        for x in pushed:
            stack.append(x)
            while len(stack):
                if stack[-1] == popped[i]:
                    stack.pop()
                    i += 1
                else:
                    break
        return len(stack) == 0 and n - i == 0




print(Solution().validateStackSequences([2,1,0], [1,2,0]))
print(Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))
print(Solution().validateStackSequences([1,2,3,4,5], [4,3,5,1,2]))
