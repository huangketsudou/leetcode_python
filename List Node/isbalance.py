from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        s=[]
        cur=root
        while cur or s:
            while cur:
                s.append(cur)
                cur=cur.left
            cur=s.pop(-1)
            res.append(cur.val)
            cur=cur.right
        return res


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        return abs(self.core(root.left)-self.core(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def core(self,root):
        if not root:return 0
        return max(1+self.core(root.left),1+self.core(root.right))


class Solution3:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        def helper(root):
            if not root:
                return 0
            left = helper(root.left) + 1
            right = helper(root.right) + 1
            #print(right, left)
            #记录可能的层次结果
            if abs(right - left) > 1: 
                self.res = False
            return max(left, right)
        helper(root)
        return self.res


t1=TreeNode(1)
t21=TreeNode(2)
t22=TreeNode(2)
t1.left=t21
t1.right=t22
t31=TreeNode(3)
t32=TreeNode(3)
t21.left=t31
t21.right=t32
t41=TreeNode(4)
t42=TreeNode(4)
t31.left=t41
t31.right=t42



k=Solution()
print(k.isBalanced(t1))
