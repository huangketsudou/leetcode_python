from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #这个问题解决的关键在于，对于i为中心的地方，其围成的面积最大为离i最近的两个小于i处高度的面积
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            # print(stack)
            # 维护一个递增的栈
            print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                tmp = stack.pop()
                res = max(res, (i - stack[-1] - 1) * heights[tmp])
            stack.append(i)
        return res


k = Solution()
print(k.largestRectangleArea([2, 1, 5, 6, 2, 3]))
