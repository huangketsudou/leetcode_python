from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if len(left) == 0:
            return n - max(right)
        if len(right) == 0:
            return max(left)
        return max(max(left), n - min(right))
