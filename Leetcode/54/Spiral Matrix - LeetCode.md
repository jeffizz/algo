---
source: https://leetcode.com/problems/spiral-matrix/description/
created: 2025-02-27T12:38:32
tags:
  - Medium
  - Review
comment: 螺旋矩阵, 还有用pop+zip巧妙旋转矩阵的巧妙解法
---
Given an `m x n` `matrix`, return _all elements of the_ `matrix` _in spiral order_.

**Example 1:**

![](assets/Spiral%20Matrix%20-%20LeetCode/spiral1.jpg)

**Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]
**Output:** [1,2,3,6,9,8,7,4,5]

**Example 2:**

![](assets/Spiral%20Matrix%20-%20LeetCode/spiral.jpg)

**Input:** matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
**Output:** [1,2,3,4,8,12,11,10,9,5,6,7]

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`