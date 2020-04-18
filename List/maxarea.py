from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        head=0
        end=len(height)-1
        maxarea=0
        while head<end:
            if height[head]<height[end]:
                maxarea=max((end-head)*height[head],maxarea)
                head+=1
            else:
                maxarea = max((end - head) * height[end], maxarea)
                end-=1
            #在这里，对于height[start]==height[end]这种情况不需要讨论。因为题目只关心最大值
            #而随着end，start之间的差距变小，中间的盛水要比两边的大，就必然有中间有两个高度大于两边
            #按上面的策略缩放两边，最终会被取到，而如果没有，那形成的面积必定小于此时的end，start形成的面积
        return maxarea
