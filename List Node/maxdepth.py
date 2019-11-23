from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        return max(1+self.maxDepth(root.left),1+self.maxDepth(root.right))


class Solution2:
    #BFS
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        s=[root]
        answer=0
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
            answer+=1
            s=tmp
        return answer


class Solution3:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth




t3=TreeNode(3)
t9=TreeNode(9)
t20=TreeNode(20)
t3.left=t9
t3.right=t20
t15=TreeNode(15)
t7=TreeNode(7)
t20.left=t15
t20.right=t7



k=Solution2()
print(k.maxDepth(t3))
