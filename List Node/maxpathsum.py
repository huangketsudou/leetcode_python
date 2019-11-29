from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        def core(root):
            nonlocal answer
            if not root:return 0
            leftgain=max(core(root.left),0) #如果子节点为负数，抛弃
            rightgain=max(core(root.right),0)
            answer=max(leftgain+root.val+rightgain,answer)
            return root.val+max(leftgain,rightgain)

        if not root: return 0
        answer = float('-inf')
        core(root)

        return answer



tn10=TreeNode(-10)
t9=TreeNode(-9)
t20=TreeNode(-20)
t15=TreeNode(-15)
t7=TreeNode(-7)
tn10.left=t9
tn10.right=t20
t20.left=t15
t20.right=t7


k=Solution()
print(k.maxPathSum(tn10))
