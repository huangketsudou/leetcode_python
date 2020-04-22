from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:return []
        answer=[]
        stack=[root]
        while stack:
            tmpstack=[]
            while stack:
                if len(stack)==1:
                    answer.append(stack[0].val)
                tmp=stack.pop(0)
                if tmp.left:
                    tmpstack.append(tmp.left)
                if tmp.right:
                    tmpstack.append(tmp.right)
            stack=tmpstack
        return answer


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        queue = collections.deque([(root, 1)])
        res, cur_level = [], 0
        while queue:
            node, level = queue.popleft()
            if node:
                if level > cur_level:
                    res.append(node.val)
                    cur_level = level
                queue.append((node.right, level + 1))
                queue.append((node.left, level + 1))
        return res
