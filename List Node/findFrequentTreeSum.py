from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.dictionary = defaultdict(int)
        self.maxtime = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right =dfs(node.right)
            summary = node.val + left + right
            self.dictionary[summary] += 1
            if self.dictionary[summary] > self.maxtime:
                self.maxtime = self.dictionary[summary]
            return summary
        dfs(root)
        ans=[]
        for key,values in self.dictionary.items():
            if values == self.maxtime:
                ans.append(key)
        return ans