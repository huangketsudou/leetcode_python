from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = deque()
        stack.append(root)
        ans = []
        while stack:
            substack = deque()
            maximun = float('-inf')
            while stack:
                node = stack.popleft()
                maximun = max(maximun,node.val)
                if node.left:
                    substack.append(node.left)
                if node.right:
                    substack.append(node.right)
            stack = substack
            ans.append(maximun)
        return ans