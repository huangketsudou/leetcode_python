from typing import List
from collections import deque


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        stack = deque()
        if not root: return []
        stack.append(root)
        ans = []
        while stack:
            stacktmp = deque()
            tmp = []
            while stack:
                node = stack.popleft()
                tmp.append(node.val)
                for child in node.children:
                    stacktmp.append(child)
            ans.append(tmp)
            stack=stacktmp
        return ans
