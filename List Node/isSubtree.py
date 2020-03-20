class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def core(node,subnode):
            if not node and not subnode:return True
            if not node or not subnode:return False
            if node.val == subnode.val:
                left=core(node.left,subnode.left)
                right=core(node.right,subnode.right)
                return left and right
            return False


        stack=deque()
        stack.append(s)
        flag=False
        while stack:
            node=stack.popleft()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            if node.val==t.val:
                flag=core(node,t)
            if flag:
                return flag
        return False


class Solution2:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def inorder(node):
            if not node:return '#'

            return '*'+str(node.val)+inorder(node.left)+inorder(node.right)

        sstr=inorder(s)
        tstr=inorder(t)
        print(sstr)
        print(tstr)
        return tstr in sstr






t3=TreeNode(3)
t4=TreeNode(4)
t1=TreeNode(1)
t2=TreeNode(2)
t5=TreeNode(5)
t3.left=t4
t3.right=t5
t4.left=t1
t4.right=t2

k=Solution2()
print(k.isSubtree(t3,t4))
