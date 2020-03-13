class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        max_time = 1
        curtime = 1
        prenode = float("inf")
        ans = []

        stack = [(root, 0)]
        while stack:
            node, flag = stack.pop()
            if node:
                if flag:
                    if node.val == prenode:
                        curtime += 1
                    else:
                        curtime = 1
                        prenode = node.val
                    if curtime == max_time:
                        ans.append(node.val)
                    if curtime > max_time:
                        ans = [node.val]
                        max_time = curtime
                else:
                    if node.right:
                        stack.append((node.right, 0))
                    stack.append((node, 1))
                    if node.left:
                        stack.append((node.left, 0))
        return ans



k=Solution()
print(k.findWords(["Hello", "Alaska", "Dad", "Peace"]))
