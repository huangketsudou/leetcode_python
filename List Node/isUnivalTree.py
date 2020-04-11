class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        left = right = True
        if root.left:
            left = root.left.val == root.val and self.isUnivalTree(root.left)
        if root.right:
            right = root.right.val == root.val and self.isUnivalTree(root.right)
        return left and right
