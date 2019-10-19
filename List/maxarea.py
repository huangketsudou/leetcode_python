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
        return maxarea
