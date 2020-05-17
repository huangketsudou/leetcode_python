class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root,float('-inf'))
        return self.ans

    def dfs(self, node, prev):
        if not node:
            return
        if node.val >= prev:
            self.ans += 1
        prev = max(node.val, prev)
        self.dfs(node.left, prev)
        self.dfs(node.right, prev)
