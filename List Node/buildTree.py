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
    #这个用前序和中序合成
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

    
class Solution3:
    #注意list.index是线性查找，最坏的情况退化到O(n**2),可以利用哈希表实现最坏O(n)
    #这个用中序和后序
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        index=postorder[-1]
        cur=inorder.index(index)
        root=TreeNode(index)
        root.left=self.buildTree(inorder[:cur],postorder[:cur])
        root.right=self.buildTree(inorder[cur+1:],postorder[cur:-1])
        return root

#前序
k=Solution()
t=k.buildTree([3,9,20,15,7],[9,3,15,20,7])


g=Solution2()
print(g.inorderTraversal(t))


#后序
k=Solution3()
t=k.buildTree([9,3,15,20,7],[9,15,7,20,3])


g=Solution2()
print(g.inorderTraversal(t))

