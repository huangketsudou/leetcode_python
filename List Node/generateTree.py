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
    #统计树的数量——超时
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

    
    
class Solution2:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        #另G代表左右子树有几个节点能有几种情况
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]


class Solution3(object):
    #卡塔兰数计算
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
    
    
    

k = Solution()
print(k.numTrees(3))
