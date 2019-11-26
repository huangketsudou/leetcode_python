from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution2:
    #题目定义的叶子节点是没有子节点的节点，而不是一个单一的路径
    #只确定是否存在
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False
        if not root.left and not root.right and sum - root.val == 0: return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)



class Solution:
    #输出路径
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        answer=[]
        self.core(root,[],answer,sum)
        return answer



    def core(self,root,tmp,answer,target):
        if not root:
            return
        if not root.left and not root.right and sum(tmp)+root.val==target:
            answer.append(tmp+[root.val])
            return
        self.core(root.left,tmp+[root.val],answer,target)
        self.core(root.right,tmp+[root.val],answer,target)


class Solution3:
    def pathSum(self, root: TreeNode, sum_: int) -> List[List[int]]:
        if not root: return []
        stack = [([root.val], root)]
        res = []
        while stack:
            tmp, node = stack.pop()
            if not node.right and not node.left and sum(tmp) == sum_:
                res.append(tmp)
            if node.right:
                stack.append((tmp + [node.right.val], node.right))
            if node.left:
                stack.append((tmp + [node.left.val], node.left))
        return res




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


k=Solution2()
print(k.hasPathSum(t5,22))


g=Solution()
print(g.pathSum(t5,22))
