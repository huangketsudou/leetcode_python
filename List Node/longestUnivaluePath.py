# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        ans = 0

        def core(node):
            nonlocal ans
            if not node: return 0
            left = core(node.left)
            right = core(node.right)
            arrowleft = arrowright = 0
            if node.left and node.val==node.left.val:
                arrowleft=left+1
            if node.right and node.val==node.right.val:
                arrowright=right+1
            ans=max(ans,arrowright+arrowleft)
            return max(arrowleft,arrowright)
        core(root)
        return ans
