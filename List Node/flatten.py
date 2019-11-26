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
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:return None
        stack=[]
        node=root
        res=[]
        while node or stack:
            while node:
                stack.append(node)
                res.append(node)
                node=node.left
            node=stack.pop(-1)
            node=node.right
        record=head=res.pop(0)
        head.left=None
        while res:
            tmp=res.pop(0)
            tmp.left=None
            head.right=tmp
            head=head.right
        return record



t5=TreeNode(5)
t41=TreeNode(4)
t8=TreeNode(8)
t5.left=t41
t5.right=t8
t11=TreeNode(11)
t13=TreeNode(13)
t42=TreeNode(4)
t41.left=t11
t8.left=t13
t8.right=t42
t7=TreeNode(7)
t2=TreeNode(2)
t52=TreeNode(5)
t1=TreeNode(1)
t11.left=t7
t11.right=t2
t42.right=t1
t42.left=t52


k=Solution()
k.flatten(t5)
t=t5
while t:
    print(t.val)
    t=t.right

