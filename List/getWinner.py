from typing import List
from collections import defaultdict


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)
        time = 0
        prev = arr[0]
        for i in range(1, n):
            if arr[i] < prev:
                time += 1
            else:
                time = 1
                prev = arr[i]
            if time == k:
                return prev
        return prev