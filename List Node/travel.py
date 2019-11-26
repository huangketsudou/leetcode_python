from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:

    def inorderTravelRecur(self,root:TreeNode):
        #递归实现中序遍历

        def core(root,answer):
            if not root:return
            core(root.left,answer)
            answer.append(root.val)
            core(root.right,answer)

        answer = []
        core(root,answer)
        return answer


    def leveltravelStack(self,root:TreeNode):
        #栈实现层遍历
        if not root:return []
        answer=[]
        stack=[root]
        while stack:
            tmp=stack.pop(0)
            if tmp.left:
                stack.append(tmp.left)
            if tmp.right:
                stack.append(tmp.right)
            answer.append(tmp.val)
        return answer


    def preTravelRecur(self,root):
        #递归实现前序遍历
        def core(root,answer):
            if not root:
                return
            answer.append(root.val)
            core(root.left,answer)
            core(root.right,answer)

        answer=[]
        core(root,answer)
        return answer


    def postTravelRecur(self,root):
        #递归实现后序遍历
        def core(root,answer):
            if not root:
                return
            core(root.left,answer)
            core(root.right,answer)
            answer.append(root.val)

        answer=[]
        core(root,answer)
        return answer


    def inorderTravelStack(self,root):
        #栈实现中序遍历
        answer=[]
        stack=[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop(-1)
            answer.append(root.val)
            root=root.right
        return answer


    def preTravelStack(self,root):
        #栈实现前序遍历
        answer=[]
        stack=[]
        while root or stack:
            while root:
                stack.append(root)
                answer.append(root.val)
                root=root.left
            root=stack.pop(-1)
            root=root.right
        return answer


    def postTravelStack(self,root):
        #利用前序遍历与后序遍历的关系实现栈后序遍历
        #前序遍历：根左右，后序遍历：左右根
        #因此利用前序遍历改变遍历顺序为根右左，再倒序输出既能得到
        answer=[]
        stack=[]
        stack2=[]
        while root or stack:
            while root:
                stack.append(root)
                stack2.append(root)
                root=root.right
            root=stack.pop(-1)
            root=root.left
        while stack2:
            answer.append(stack2.pop(-1).val)
        return answer

t5=TreeNode(5)
t41=TreeNode(4)
t8=TreeNode(8)
t5.left=t41
t5.right=t8
t11=TreeNode(11)
t13=TreeNode(13)
t42=TreeNode(4)
t41.left=t11
t8.left=t13
t8.right=t42
t7=TreeNode(7)
t2=TreeNode(2)
t52=TreeNode(5)
t1=TreeNode(1)
t11.left=t7
t11.right=t2
t42.right=t1
t42.left=t52



k=Solution()
print(k.postTravelRecur(t5))
