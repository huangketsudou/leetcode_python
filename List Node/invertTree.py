from typing import List
from collections import deque



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:return root
        if not root.left and not root.right:return root
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:return root
        stack=deque()
        stack.append(root)
        while stack:
            node=stack.popleft()
            if node.left:stack.append(node.left)
            if node.right:stack.append(node.right)
            node.left,node.right=node.right,node.left
        return root


class Solution3:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        answer=[]
        if root:
            s=[root]
        else:
            s=[]
        while s:
            tmpans=[]
            tmp=[]
            while s:
                curr=s.pop(0)
                tmpans.append(curr.val)
                if curr.left:
                    tmp.append(curr.left)
                if curr.right:
                    tmp.append(curr.right)
            answer.append(tmpans)
            s=tmp
        return answer


t3=TreeNode(3)
t9=TreeNode(9)
t20=TreeNode(20)
t3.left=t9
t3.right=t20
t15=TreeNode(15)
t7=TreeNode(7)
t20.left=t15
t20.right=t7
t1=TreeNode(1)
t2=TreeNode(2)
t9.left=t1
t9.right=t2

k=Solution3()
print(k.levelOrder(t3))

g=Solution2()
g.invertTree(t3)

print(k.levelOrder(t3))
