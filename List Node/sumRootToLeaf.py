class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ans=0
    def sumRootToLeaf(self, root: TreeNode) -> int:
        MOD=10^9+7
        def core(node,tmp):
            if not node.left and not node.right:
                self.ans+=(tmp*2+node.val)%MOD
            if node.left:
                core(node.left,(2*tmp+node.val)%MOD)
            if node.right:
                core(node.right,(2*tmp+node.val)%MOD)

        if not root:return 0

        core(root,0)
        return self.ans






