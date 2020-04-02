from itertools import combinations
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        #海伦公式
        return max(abs((x0-x2)*(y1-y2)-(x1-x2)*(y0-y2)) for (x0,y0),(x1,y1),(x2,y2) in combinations(points,3))/2

