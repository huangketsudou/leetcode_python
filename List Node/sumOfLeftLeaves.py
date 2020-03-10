from collections import deque
from collections import Counter
from itertools import combinations,product

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result=[]
        def core(node,flag,result):
            if not node.left and not node.right and flag:
                result.append(node.val)
                return
            if node.left:
                core(node.left,True,result)
            if node.right:
                core(node.right,False,result)

        core(root,False,result)
        return sum(result)

class Solution2:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:return 0

        result=0
        stack=deque()
        stack.append((root,False))
        while stack:
            node,flag=stack.popleft()
            if not node.left and not node.right and flag:
                result+=node.val
            if node.left:
                stack.append((node.left,True))
            if node.right:
                stack.append((node.right,False))
        return result



t3=TreeNode(3)
t9=TreeNode(9)
t20=TreeNode(20)
t15=TreeNode(15)
t7=TreeNode(7)
t3.left=t9
t3.right=t20
t20.left=t15
t20.right=t7

k=Solution2()
print(k.sumOfLeftLeaves(t3))
