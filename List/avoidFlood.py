from typing import List
from collections import defaultdict
import bisect


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        visited = defaultdict()  # 下了雨的湖
        empty = []  # 没下雨的日子
        result = []  # 结果
        for i, rain in enumerate(rains):
            if rain > 0:
                if rain in visited:
                    if len(empty) != 0:
                        idx_day = bisect.bisect_left(empty, visited[rain])
                        if idx_day >= len(empty): return []
                        day = empty[idx_day]
                        result[day] = rain
                        empty.remove(day)
                    else:
                        return []
                result.append(-1)
                visited[rain] = i
            else:
                empty.append(i)
                result.append(1)
        return result


k = Solution()
print(k.avoidFlood([0, 1, 1]))
