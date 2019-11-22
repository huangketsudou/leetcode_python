from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p==None and q==None:return True
        if p and q and p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False


qt1=TreeNode(1)
qt2=TreeNode(2)
qt1.left=qt2

pt1=TreeNode(1)
pt2=TreeNode(2)
pt1.right=pt2



k=Solution()
print(k.isSameTree(pt1,qt1))
