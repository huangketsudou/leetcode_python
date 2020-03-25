# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:return [0]
        stack = [root]
        ans=[]
        while stack:
            tmp=[]
            count=0
            res=0
            while stack:
                node=stack.pop()
                res+=node.val
                count+=1
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            ans.append(res/count)
            stack=tmp
        return ans
