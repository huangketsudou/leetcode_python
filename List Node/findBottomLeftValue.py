from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        target = -1
        stack = deque(root)
        while stack:
            node = stack.popleft()
            target = node.val
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return target
