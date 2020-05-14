from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        prev = float('-inf')
        ans = 0
        for start, end in points:
            if start > prev:
                ans+=1
                prev=end
        return ans

