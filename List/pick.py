from typing import List
import random
import bisect


class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.size = len(rects)
        self.weight = []
        s = 0
        for a, b, c, d in rects:
            area = (c - a + 1) * (d - b + 1)  # 每个只会选择左上角的点
            s += area
            self.weight.append(s)

    def pick(self) -> List[int]:
        index = bisect.bisect_left(self.weight, random.randint(1, self.weight[-1]))
        x1, y1, x2, y2 = self.rects[index]
        return [random.randint(x1, x2), random.randint(y1, y2)]
