from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        [x1, y1], [x2, y2], [x3, y3] = points
        return (y2 - y1) * (x3 - x1) != (x2 - x1) * (y3 - y1)
