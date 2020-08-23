from typing import List
from collections import defaultdict


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        visited = defaultdict(int)
        for i in range(1, len(rounds)):
            start = rounds[i - 1]
            end = rounds[i]
            while start != end:
                visited[start] += 1
                start = n if (start + 1) % n == 0 else (start + 1) % n
        visited[start] += 1
        M = max(visited.values())
        ans = []
        for k,v in visited.items():
            if v == M:
                ans.append(k)
        ans.sort()
        return ans


class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        s, e = rounds[0], rounds[-1]
        if s <= e:
            # [起点, 终点]
            return list(range(s, e + 1))
        else:
            # [1, 终点]+[起点, n]
            return list(range(1, e + 1)) + list(range(s, n + 1))

