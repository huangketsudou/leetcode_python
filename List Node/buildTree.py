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
    #注意list.index是线性查找，最坏的情况退化到O(n**2),可以利用哈希表实现最坏O(n)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        index=preorder[0]
        cur=inorder.index(index)
        root=TreeNode(index)
        root.left=self.buildTree(preorder[1:1+cur],inorder[:cur])
        root.right=self.buildTree(preorder[1+cur:],inorder[cur+1:])
        return root



k=Solution()
t=k.buildTree([3,9,20,15,7],[9,3,15,20,7])


g=Solution2()
print(g.inorderTraversal(t))




