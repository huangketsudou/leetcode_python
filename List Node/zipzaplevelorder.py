from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        answer=[]
        if root:
            s=[root]
        else:
            s=[]
        dir=1
        while s:
            tmpans=[]
            tmp=[]
            while s:
                curr=s.pop(-1)
                tmpans.append(curr.val)
                if dir:
                    if curr.left:
                        tmp.append(curr.left)
                    if curr.right:
                        tmp.append(curr.right)
                else:
                    if curr.right:
                        tmp.append(curr.right)
                    if curr.left:
                        tmp.append(curr.left)
            answer.append(tmpans)
            s=tmp
            dir=1-dir
        return answer







t3=TreeNode(3)
t9=TreeNode(9)
t20=TreeNode(20)
t3.left=t9
t3.right=t20
t15=TreeNode(15)
t7=TreeNode(7)
t20.left=t15
t20.right=t7


k=Solution()
print(k.zigzagLevelOrder(t3))
