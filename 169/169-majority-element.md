---
created: 2025-01-30T11:20:21
---
## Problem
Given an array `nums` of size `n`, return _the majority element_.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

**Input:** `nums = [3,2,3]`
**Output:** 3

**Example 2:**

**Input:** `nums = [2,2,1,1,1,2,2]`
**Output:** 2

**Constraints:**

- `n == nums.length`
- `1 <= n <= 5 * 104`
- `-109 <= nums[i] <= 109`

**Follow-up:** Could you solve the problem in linear time and in `O(1)` space?

## Solution
To solve the problem of finding the majority element in an array (the element that appears more than ⁠⌊n / 2⌋ times) in linear time and constant space, we can use the **Boyer-Moore Voting Algorithm**. This algorithm is efficient and works based on the concept of counting votes for potential candidates.

**Boyer-Moore Voting Algorithm**

The algorithm works in two main steps:

1. **Candidate Selection**: Traverse through the array and maintain a candidate for the majority element and a counter. If the counter is zero, we select the current element as the new candidate. If the current element is the same as the candidate, we increment the counter; otherwise, we decrement it.

2. **Result**: Since the problem guarantees that a majority element always exists, the candidate at the end of the traversal will be the majority element.

**Implementation**

Here’s how you can implement this algorithm in Python:
```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        
        # Step 1: Find the candidate for majority element
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        # Step 2: The candidate is the majority element
        return candidate
```