from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        def core(node1,node2):
            if node1==None and node2==None:
                return True
            if node1 and node2 and node1.val==node2.val:
                return core(node1.left,node2.right) and core(node1.right,node2.left)
            return False

        return core(root.left,root.right)


class Solution2:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            if p and q and p.val != q.val:
                return False
            return True

        from collections import deque

        queue=deque([(root.left,root.right),])
        while queue:
            p,q=queue.popleft()
            if not check(p,q):
                return False
            if p:
                queue.append((p.left,q.right))
                queue.append((p.right,q.left))
        return True


t1=TreeNode(1)
t21=TreeNode(2)
t22=TreeNode(2)
t1.left=t21
t1.right=t22
t31=TreeNode(3)
t32=TreeNode(3)
t41=TreeNode(4)
t42=TreeNode(4)
t21.left=t31
t21.right=t41
t22.left=t42
t22.right=t32


k=Solution2()
print(k.isSymmetric(t1))
