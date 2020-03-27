class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        h = [-float('inf'), -float('inf')]
        def f(r):
            if r:
                -r.val not in h and heapq.heappushpop(h, -r.val)
                f(r.left)
                f(r.right)
        f(root)
        return h[0] == -float('inf') and -1 or -h[0]


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # 直觉: BFS/DFS找到所有第一次比根节点大的,取min:
        # BFS Done

        res = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if not node:
                continue

            if node.val == root.val:
                queue.append(node.left)
                queue.append(node.right)
            else:
                res.append(node.val)

        return -1 if not res else min(res)


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        judge = root.val
        def find(root):
            if not root:
                return 1000000000000
            if root.val == judge:
                return min(find(root.left),find(root.right))
            return min(root.val,find(root.left),find(root.right))
        second = find(root)
        return second if second !=1000000000000 else -1

