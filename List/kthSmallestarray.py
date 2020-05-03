from typing import List
from collections import deque
import heapq


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m = len(mat)
        n = len(mat[0])
        stack = []
        choice = [0] * m
        ans = 0
        for i in range(m):
            ans += mat[i][0]
        stack.append((ans, choice))
        seen = set()
        while k != 0:
            ans, node = heapq.heappop(stack)
            print(node,ans)
            if k>0:
                for i in range(m):
                    if node[i] + 1 < n:
                        tmp = ans - mat[i][node[i]]
                        node[i] += 1
                        if tuple(node) not in seen:
                            heapq.heappush(stack, (tmp + mat[i][node[i]], node[:]))
                            seen.add(tuple(node))
                        node[i] -= 1
            k -= 1
        return ans


k = Solution()
print(k.kthSmallest(mat = [[1,3,11],[2,4,6]], k = 5))
