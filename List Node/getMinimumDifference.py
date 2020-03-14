# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if not root:return 0
        if not root.left and not root.right:return 0
        stack=deque()
        node=root
        prev=None
        res=float('inf')
        while stack or node:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            if prev is None:
                prev=node.val
            else:
                res=min(node.val-prev,res)
                prev=node.val
            node=node.right
        return res
