class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rob(self, root: TreeNode) -> int:

        memo = {}

        def core(root):
            if not root: return 0
            if root in memo: return memo[root]
            left = self.rob(root.left)
            right = self.rob(root.right)
            ll, lr = [self.rob(root.left.left), self.rob(root.left.right)] if root.left else [0, 0]
            rl, rr = [self.rob(root.right.left), self.rob(root.right.right)] if root.right else [0, 0]

            result = max(root.val + ll + lr + rl + rr, left + right)
            memo[root] = result
            return result

        return core(root)


class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root: return 0
        left = self.rob(root.left)
        right = self.rob(root.right)
        ll, lr = [self.rob(root.left.left), self.rob(root.left.right)] if root.left else [0, 0]
        rl, rr = [self.rob(root.right.left), self.rob(root.right.right)] if root.right else [0, 0]

        return max(root.val + ll + lr + rl + rr, left + right)


class Solution:
    #树形dp，取与不取
    def rob(self, root: TreeNode) -> int:
        def dp(node):
            if not node: return [0, 0]
            left = dp(node.left)
            right = dp(node.right)
            return [max(left) + max(right),node.val + left[0] + right[0]]

        return max(dp(root))


class Solution:

    def dp(self, cur: TreeNode) -> List[int]:
        if not cur:
            return [0, 0]

        l = self.dp(cur.left)
        r = self.dp(cur.right)

        return [max(l) + max(r), cur.val + l[0] + r[0]]

    def rob(self, root: TreeNode) -> int:
        return max(self.dp(root))


