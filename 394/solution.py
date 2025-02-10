#!/usr/bin/env python3

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        k = ""
        st = ""
        nst = ""
        for c in s:
            if str.isdigit(c):
                k += c
                if not stack:
                    nst += st
                    st = ""
            if str.isalpha(c):
                st += c
            if c == '[':
                if st: stack.append(st)
                st = ""
                stack.append(k)
                k = ""
            if c == ']':
                while stack and str.isalpha(stack[-1]):
                    st = stack.pop() + st
                if stack and str.isdigit(stack[-1]):
                    st = st * int(stack.pop())
                if stack: stack.append(st)
                else: nst += st
                st = ""
        return nst + st



print(Solution().decodeString('3[a]2[bc]'))
print(Solution().decodeString('3[a2[c]]'))
print(Solution().decodeString('2[abc]3[cd]ef'))
print(Solution().decodeString('abc3[cd]xyz'))
print(Solution().decodeString('3[z]2[2[y]pq4[2[jk]e1[f]]]ef'))
