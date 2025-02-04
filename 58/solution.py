#!/usr/bin/env python3

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        i,count = 1, 1
        while i < length:
            if s[i-1] == ' ' and s[i] != ' ':
                count = 1
            if s[i-1] != ' ' and s[i] != ' ':
                count += 1
            i += 1
        return count

    def lengthOfLastWord2(self, s: str) -> int:
        trimmed_s = s.strip()
        words = trimmed_s.split()
        last_word = words[-1]
        return len(last_word)


s = 'Hello World'
print(Solution().lengthOfLastWord(s))
s = '   fly me   to   the moon  '
print(Solution().lengthOfLastWord(s))
s = 'Hello'
print(Solution().lengthOfLastWord(s))
