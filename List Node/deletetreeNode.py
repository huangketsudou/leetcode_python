class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None: return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val <key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left:
                parent, child = root, root.left
                while child.right is not None:
                    parent = child
                    child = child.right
                if parent != root:
                    parent.right=child.left
                    child.left = root.left
                    child.right = root.right
                    root = child
                else:
                    child.right = root.right
                    root = child
            elif root.right:
                parent, child = root, root.right
                while child.left is not None:
                    parent = child
                    child = child.left
                if parent != root:
                    parent.left = child.right
                    child.right = root.right
                    child.left = root.left
                    root = child
                else:
                    child.left = root.left
                    root = child
            else:
                root = None
        return root
