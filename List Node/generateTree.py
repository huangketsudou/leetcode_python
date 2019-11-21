# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #生成具体的树结构
    def generateTrees(self, n: int) -> List[TreeNode]:
        
        def generate_trees(start, end):
            if start > end:
                return [None, ]

            all_trees = []
            for i in range(start, end + 1):  # pick up a root
                # all possible left subtrees if i is choosen to be a root
                left_trees = generate_trees(start, i - 1)

                # all possible right subtrees if i is choosen to be a root
                right_trees = generate_trees(i + 1, end)

                # connect left and right subtrees to the root i
                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)

            return all_trees

        return generate_trees(1, n) if n else []
        
        
        
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    #统计树的数量
    def numTrees(self, n: int) -> int:
        answer = self.core(1, n)

        return answer

    def core(self, start, end):
        if start > end:
            return 1
        else:
            res = 0
            for i in range(start, end + 1):
                left = self.core(start, i - 1)
                right = self.core(i + 1, end)
                res += left * right
        return res


k = Solution()
print(k.numTrees(3))
