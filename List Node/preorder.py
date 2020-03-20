class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:


        if not root:return []
        res=[root.val]
        for child in root.children:
            res+=self.preorder(child)
        return res


class Solution2:
    def preorder(self, root: 'Node') -> List[int]:
        from collections import deque

        stack=deque()
        stack.append(root)
        res=[]
        while stack:
            node=stack.popleft()
            res.append(node.val)
            if node.children is not None:
                for child in reversed(node.children):
                    stack.appendleft(child)

        return res


class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])#!!!!!!!

        return output
