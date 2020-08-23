from typing import List
from collections import defaultdict


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        self.dp = [-1] * (n + 2)
        self.count = defaultdict(int)
        self.number = defaultdict(int)
        last = -1
        for i, v in enumerate(arr):
            self.dp[v] = v
            self.count[v] = 1
            self.number[1] += 1
            if self.dp[v - 1] != -1:
                self.union(v, v - 1)
            if self.dp[v + 1] != -1:
                self.union(v + 1, v)
            # if m in set(self.count.values()):
            #     last = i + 1
            # for k in self.count.values():
            #     if k == m:
            #         last = i + 1
            #         break
            if self.number[m] != 0:
                last = i + 1
        return last

    def union(self, child, parent):
        parent = self.find(parent)
        child = self.find(child)
        self.dp[child] = parent
        self.number[self.count[parent]] -= 1
        self.count[parent] += self.count[child]
        self.number[self.count[parent]] += 1
        self.number[self.count[child]] -= 1
        del self.count[child]

    def find(self, x):
        if self.dp[x] != x:
            self.dp[x] = self.find(self.dp[x])
        return self.dp[x]


k = Solution()
print(k.findLatestStep([2,1], 2))


