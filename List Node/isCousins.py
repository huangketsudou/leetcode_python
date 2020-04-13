from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        iscousins=[]
        stack=deque()
        stack.append((None,root,0))
        while stack:
            parent,node,d=stack.popleft()
            if node.val==x or node.val==y:
                iscousins.append((parent,node.val,d))
            if len(iscousins)==2:break
            if node.left:
                stack.append((node,node.left,d+1))
            if node.right:
                stack.append((node,node.right,d+1))
        f,b=iscousins
        return f[0]!=b[0] and f[2]==b[2]
