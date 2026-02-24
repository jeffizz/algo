#!/usr/bin/env python3

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        r = []
        i = 0;
        while matrix:
            # 方法有效,但频繁的切片操作, 也会带来复杂性, 可以用指针代替
            if i == 0:# → 转 ↓
                j = len(matrix[i]) - 1
                r.extend(matrix[i])
                matrix = matrix[i+1:]
                while i < len(matrix):
                    if len(matrix[i]): # j 不变, i 递增
                        r.append(matrix[i][j])
                        matrix[i] = matrix[i][:j]
                    i += 1
            else: # ← 转 ↑
                matrix[i-1].reverse()
                r.extend(matrix[i-1])
                matrix = matrix[:i-1]
                i -= 1
                while i > 0:
                    if len(matrix[i-1]): # j 为 0, i 递减
                        r.append(matrix[i-1][0])
                        matrix[i-1] = matrix[i-1][1:]
                    i -= 1
        return r

# print(Solution().spiralOrder([[1,2,3]]))
# print(Solution().spiralOrder([[7],[9],[6]]))
# print(Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
# print(Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(Solution().spiralOrder([[ 1, 2, 3, 4],
                              [ 5, 6, 7, 8],
                              [ 9,10,11,12],
                              [13,14,15,16],
                              [17,18,19,20],
                              [21,22,23,24]]))
