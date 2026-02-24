#!/usr/bin/env python3

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    # 解法二: 使用队列进行BFS遍历
        if root is None:
            return root
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            tmp = node.left
            node.left = node.right
            node.right = tmp
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return root


    # 解法一: 使用递归分治 O(n), O(n)
        # if root is None:
        #     return root
        # if root.left is not None or root.right is not None:
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
        # node = root.left
        # root.left = root.right
        # root.right = node
        # return root

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

print(
    Solution().bst_to_list(
        Solution().invertTree(
            Solution().list_to_bst([2,1,3])
        )
    )
)

print(
    Solution().bst_to_list(
        Solution().invertTree(
            Solution().list_to_bst([4,2,7,1,3,6,9])
        )
    )
)
