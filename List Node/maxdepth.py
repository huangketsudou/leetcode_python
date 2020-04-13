from collections import deque

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:return 0
        d=0
        stack=deque()
        stack.append((root,d+1))
        
        while stack:
            node,d=stack.popleft()
            for n in node.children:
                stack.append((n,d+1))
        
        return d
