# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def iterator(root):
            if root:
                if root.left is None and root.right is None:
                    yield root.val
                yield from iterator(root.left)
                yield from iterator(root.right)

        r1=list(iterator(root1))
        r2=list(iterator(root2))
        return r1==r2   
