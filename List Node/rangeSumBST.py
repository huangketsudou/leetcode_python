class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans=0
        def dfs(node):
            if node:
                if L<=node.val<=R:
                    self.ans+=node.val
                if L<node.val:
                    dfs(node.left)
                if R>node.val:
                    dfs(node.right)
        dfs(root)
        return self.ans




class Solution2:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

        stack=deque()
        stack.append(root)
        ans=0
        while stack:
            node=stack.popleft()
            if node:
                if L<=node.val<=R:
                    ans+=node.val
                if L<node.val:
                    stack.append(node.left)
                if R>node.val:
                    stack.append(node.right)
        return ans
