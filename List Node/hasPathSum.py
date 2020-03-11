# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.core(root,0,sum)


    def core(self,root,tmp,target):
        if not root:
            return False
        if not root.left and not root.right :
            return tmp+root.val==target
        return self.core(root.left,tmp+root.val,target) or self.core(root.right,tmp+root.val,target)
        
        
 class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        answer=[]
        self.core(root,[],answer,sum)
        return answer



    def core(self,root,tmp,answer,target):
        if not root:
            return
        if not root.left and not root.right and sum(tmp)+root.val==target:
            answer.append(tmp+[root.val])
            return
        self.core(root.left,tmp+[root.val],answer,target)
        self.core(root.right,tmp+[root.val],answer,target)
        
        
        
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        from collections import deque
        if not root:return 0
        res=0
        stack=deque()
        stack.append((root,0))
        head=set()
        head.add(root)
        while stack:
            node,summary=stack.popleft()
            nxtsum=summary+node.val
            print(nxtsum)
            if nxtsum==sum:
                res+=1
            if node.left:
                stack.append((node.left,nxtsum))
                if node.left not in head:
                    stack.append((node.left, 0))
                    head.add(node.left)
            if node.right:
                stack.append((node.right,nxtsum))
                if node.right not in head:
                    stack.append((node.right, 0))
                    head.add(node.right)
        return res
