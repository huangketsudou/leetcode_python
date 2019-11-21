from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:return []
        res=[]
        self.core(root,res)
        return res


    def core(self,node,res):
        if node==None:
            return
        else:
            self.core(node.left,res)
            res.append(node.val)
            self.core(node.right,res)


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


t3=TreeNode(3)
t2=TreeNode(2)
t2.left=t3
t1=TreeNode(1)
t1.right=t2

k=Solution2()
print(k.inorderTraversal(t1))
