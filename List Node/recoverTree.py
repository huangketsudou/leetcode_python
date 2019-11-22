from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solutioninorder:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        s=[]
        cur=root
        while cur or s:
            while cur:
                s.append(cur)
                cur=cur.left
            cur=s.pop(-1)
            res.append(cur.val)
            cur=cur.right
        return res


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        firstNode = None
        secondNode = None
        pre = TreeNode(float("-inf"))

        stack = []
        p = root
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()

            if not firstNode and pre.val > p.val:
                firstNode = pre
            if firstNode and pre.val > p.val:
                # print(firstNode.val,pre.val, p.val)
                secondNode = p
            pre = p
            p = p.right
        firstNode.val, secondNode.val = secondNode.val, firstNode.val



class Solution2:
    def recoverTree(self, root: TreeNode) -> None:
        first = None
        second = None
        pre = None
        curr = root
        while curr:
            if curr.left == None:
                if pre != None and pre.val > curr.val:
                    if first == None:
                        first = pre
                        second = curr
                    else:
                        second = curr
                pre = curr
                curr = curr.right
            else:
                tmp = curr.left
                while tmp.right != None and tmp.right != curr:  # != curr用于找到当前的curr
                    tmp = tmp.right
                if tmp.right == None:  # 子树的最右节点附上下一节点
                    tmp.right = curr
                    curr = curr.left
                else:
                    tmp.right = None  # 恢复树形状
                    if pre != None and pre.val > curr.val:
                        if first == None:
                            first = pre
                            second = curr
                        else:
                            second = curr
                    pre = curr
                    curr = curr.right
        first.val, second.val = second.val, first.val


t1=TreeNode(1)
t3=TreeNode(3)
t1.left=t3
t2=TreeNode(2)
t3.right=t2

#
k=Solution()
a=k.recoverTree(t1)


g=Solutioninorder()
print(g.inorderTraversal(t1))
