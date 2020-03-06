from typing import List
from collections import deque
import heapq
import functools

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:return []
        result=[]
        tmp=[]
        self.core(tmp,root,result)
        return result


    def core(self,tmp,node,result):
        if not node.left and not node.right:
            tmp.append(str(node.val))
            result.append('->'.join(tmp))
        if node.left:
            self.core(tmp+[str(node.val)],node.left,result)
        if node.right:
            self.core(tmp+[str(node.val)],node.right,result)


class Solution2:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        :Bfs
        """
        if not root:
            return []

        paths = []
        stack = [(root, str(root.val))]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                paths.append(path)
            if node.left:
                stack.append((node.left, path + '->' + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + '->' + str(node.right.val)))

        return paths





t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(3)
t5=TreeNode(5)
t1.left=t2
t1.right=t3
t2.right=t5


k=Solution()
print(k.binaryTreePaths(t1))
