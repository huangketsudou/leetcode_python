class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        res = 0
        for x1, y1 in points:
            lookup = dict()
            for x2, y2 in points:
                if x1 == x2 and y1 == y2: continue
                dx = x1-x2
                dy = y1-y2
                dis = dx*dx + dy*dy
                if dis not in lookup:
                    lookup[dis] = 1
                else:
                    res += lookup[dis]
                    lookup[dis] += 1
        return res * 2


from collections import Counter
from scipy.special import perm


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        count = 0
        for point in points:

            # distance2 记录对这个点来说的所有的距离
            distance2 = []
            for neighbor in points:
                distance2.append((point[0] - neighbor[0]) ** 2 + (point[1] - neighbor[1]) ** 2)

            frequency = Counter(distance2)

            for dist, num in frequency.items():
                if num >= 2:
                    count += perm(num, 2)

        return int(count)
