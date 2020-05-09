from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        from collections import deque
        bank = set(bank)
        if end not in bank:
            return -1
        visited = set()
        visited.add(start)
        mutation = {"A", "C", "G", "T"}

        # 产生只差一个字母的基因
        def oneMutation(cur):
            for i, val in enumerate(cur):
                for t in mutation - {val}:
                    tmp = cur[:i] + t + cur[i + 1:]
                    if tmp in bank:
                        yield tmp

        queue = deque()
        queue.appendleft([start, 0])
        while queue:
            cur, res = queue.pop()
            if cur == end:
                return res
            for nxt in oneMutation(cur):
                if nxt not in visited:
                    visited.add(nxt)
                    queue.appendleft((nxt, res + 1))
        return -1

