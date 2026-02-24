#!/usr/bin/env python3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left_h = self.maxDepth(root.left)
            right_h = self.maxDepth(root.right)
            return max(left_h, right_h) + 1

    def list_to_bst(self, lst):
        if not lst:
            return None

        root = TreeNode(lst[0])
        queue = [root]
        index = 1

        while index < len(lst):
            current = queue.pop(0)

            if index < len(lst) and lst[index] is not None:
                current.left = TreeNode(lst[index])
                queue.append(current.left)
            index += 1

            if index < len(lst) and lst[index] is not None:
                current.right = TreeNode(lst[index])
                queue.append(current.right)
            index += 1

        return root

    def bst_to_list(self, root):
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append(None)

        while result and result[-1] is None:
            result.pop()

        return result
