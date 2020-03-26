# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root.left and not root.right:return False
        store=self.inorder(root)
        n=len(store)
        left,right=0,n-1
        while left<right:
            tmp=store[left]+store[right]
            if tmp==k:
                return True
            elif tmp<k:
                left+=1
            else:
                right-=1
        return False
    


    def inorder(self,node):
        res=[]
        stack=[]
        while node or stack:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            res.append(node.val)
            node=node.right
        return res
