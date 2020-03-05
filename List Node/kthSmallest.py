from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        node = root
        result = []
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result.append(node.val)
            node = node.right
        return result[k - 1]


class Solution2:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            if k == 1:
                return node.val
            k -= 1
            node=node.right


t3 = TreeNode(3)
t9 = TreeNode(9)
t20 = TreeNode(20)
t3.left = t9
t3.right = t20
t15 = TreeNode(15)
t7 = TreeNode(7)
t20.left = t15
t20.right = t7

k = Solution2()
print(k.kthSmallest(t3, 1))
