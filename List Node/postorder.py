"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        from collections import deque
        if not root: return []
        stack = deque()
        stack.append(root)
        res = []
        while stack:
            node = stack.popleft()
            res.append(node.val)
            if node.children is not None:
                for child in node.children:
                    stack.appendleft(child)
        res=list(reversed(res))
        return res
