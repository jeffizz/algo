#!/usr/bin/env python3

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 解法二: 递归, 移动指针左右同时进行比较
        pass


        # 解法一: BFS,广度优先遍历, 分别比较每一层,
        # 时间复杂度: O(N) 每一层都遍历对应层的元素
        # 空间复杂度: O(N) 因为最坏情况会有取出来的最后一层全None,这种情况的最后一层的节点数为N+1个了
        if root is None:
            return True
        dq = deque()
        dq.append(root.left)
        dq.append(root.right)
        i = 1
        while True:
            arr = []
            while dq and len(arr) < 2 ** i:
                node = dq.popleft()
                if node:
                    arr.append(node.val)
                    dq.append(node.left)
                    dq.append(node.right)
                else:
                    arr.append(None)
                    dq.append(None)
                    dq.append(None)
            i += 1
            if arr[:len(arr) // 2] != arr[-(len(arr) // 2):][::-1]:
                return False
            if all(e is None for e in arr):
                return True
        return True

    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     if root is None:
    #         return True
    #     if root.left is None and root.right is None:
    #         return True
    #     if root.left is None or root.right is None:
    #         return False
    #     if root.left.val != root.right.val:
    #         return False
    #     ll = self.inorder(root.left)
    #     lr = self.inorder(root.right)
    #     count = len(ll)
    #     if len(lr) != count:
    #         return False
    #     for i in range(count):
    #         if ll[i] != lr.pop():
    #             return False
    #     return True
    #
    #
    # def inorder(self, root: Optional[TreeNode]) -> list:
    #     result = []
    #     stack = []
    #     current = root
    #     while stack or current:
    #         # 左边节点入栈,遍历到最左边的节点
    #         while current:
    #             stack.append(current)
    #             current = current.left
    #         # 访问节点
    #         current = stack.pop()
    #         if current.left is None and current.right is not None:
    #             result.append(None)
    #         result.append(current.val)
    #         # 转到右子树, 考虑current是叶节点的情况, 下次遍历就不会进到内重while循环
    #         if current.left is not None and current.right is None:
    #             result.append(None)
    #         current = current.right
    #
    #     print(result)
    #     return result
    #
    #
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
    Solution().isSymmetric(
        Solution().list_to_bst([5,2,2,4,None,None,1,None,1,None,4,2,None,2,None])
    )
)

print(
    Solution().isSymmetric(
        Solution().list_to_bst([1,2,2,2,None,2])
    )
)

print(
    Solution().isSymmetric(
        Solution().list_to_bst([1,2,2,3,4,4,3])
    )
)

print(
    Solution().isSymmetric(
        Solution().list_to_bst([1,2,2,None,3,None,3])
    )
)
