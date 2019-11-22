from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        mini=float('-inf')
        tmp = []
        now=root
        while tmp or now:
            while now:
                tmp.append(now)
                now=now.left
            now=tmp.pop(-1)
            if now.val>mini:
                mini=now.val
            else:
                return False
            now=now.right
        return True


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        self.pre = None
        def isBST(root):
            if not root:
                return True
            if not isBST(root.left):
                return False
            if self.pre and self.pre.val >= root.val:
                return False
            self.pre = root
            #print(root.val)
            return  isBST(root.right)
        return isBST(root)


class Solution3:
    def isValidBST(self, root: TreeNode) -> bool:
        def isBST(root, min_val, max_val):
            if root == None:
                return True
            # print(root.val)
            if root.val >= max_val or root.val <= min_val:
                return False
            return isBST(root.left, min_val, root.val) and isBST(root.right, root.val, max_val)
        return isBST(root, float("-inf"), float("inf"))



t1=TreeNode(1)
t3=TreeNode(3)
t2=TreeNode(2)
t2.left=t1
t2.right=t3


k=Solution()
print(k.isValidBST(t2))
