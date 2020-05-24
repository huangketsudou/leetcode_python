from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def dfs(node, tmp):
            if not node.left and not node.right:
                count = set()
                for num in tmp:
                    if num not in count:
                        count.add(num)
                    else:
                        count.remove(num)
                if len(count) <= 1:
                    self.ans += 1
                return
            if node.left:
                dfs(node.left, tmp + [node.val])
            if node.right:
                dfs(node.right, tmp + [node.val])

        dfs(root, [root.val])
        return self.ans
