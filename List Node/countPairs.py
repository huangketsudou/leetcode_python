class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.ans = 0

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.dfs(root,distance)
        return self.ans

    def dfs(self, node, distance):
        if not node:
            return []
        if not node.left and not node.right:
            return [1]
        left = self.dfs(node.left,distance)
        right = self.dfs(node.right,distance)
        for i in left:
            for j in right:
                if i + j <= distance:
                    self.ans += 1
        tmp = []
        left.extend(right)
        for k in left:
            if k + 1 <= distance:
                tmp.append(k+1)
        return tmp

k=Solution()
print(k)