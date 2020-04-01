class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:

        stack=deque()
        node=root
        prev=float('inf')
        ans=float('inf')
        while node or stack:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            ans=min(ans,abs(prev-node.val))
            prev=node.val
            node=node.right
        return ans
