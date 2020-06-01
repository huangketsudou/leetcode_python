from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        prev = 0
        heights = set()
        for i in sorted(horizontalCuts):
            heights.add(i - prev)
            prev = i
        heights.add(h - prev)
        width = set()
        prev = 0
        for j in sorted(verticalCuts):
            width.add(j- prev)
            prev = j
        width.add(w - prev)
        heights = list(heights)
        width = list(width)
        heights.sort()
        width.sort()
        return heights[-1]*width[-1]

k=Solution()
print(k.maxArea())