#!/usr/bin/env python3

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for str in strs:
            new_prefix = ''
            for s1, s2 in zip(prefix, str):
                if s1 == s2:
                    new_prefix += s1
                else:
                    break;
            prefix = new_prefix
            if prefix == '':
                break;
        return prefix

strs = ["flower","flow","flight"]
print(Solution().longestCommonPrefix(strs))
