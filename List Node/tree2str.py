class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:

        def core(node):
            if not node.left and not node.right:
                return str(node.val)
            if not node.left:
                return str(node.val)+'()'+'('+core(node.right)+')'
            if not node.right:
                return str(node.val)+'('+core(node.left)+')'
            return str(node.val)+'('+core(node.left)+')'+'('+core(node.right)+')'

        return core(t)

class Solution3:
    def tree2str(self, t: TreeNode) -> str:
        if not t:return ''
        from collections import deque
        stack=deque()
        stack.append(t)
        visited=set()
        res=''
        while stack:
            t=stack[-1]
            if t in visited:
                stack.pop()
                res+=')'
            else:
                visited.add(t)
                res+="("+str(t.val)
                if t.left is None and t.right is not None:
                    res+='()'
                if t.right is not None:
                    stack.append(t.right)
                if t.left is not None:
                    stack.append(t.left)
        return res[1:len(res)-1]


t1=TreeNode(1)
t2=TreeNode(2)
t3=TreeNode(3)
t1.left=t2
t1.right=t3
t4=TreeNode(4)
t2.right=t4

k=Solution3()
print(k.tree2str(t1))
