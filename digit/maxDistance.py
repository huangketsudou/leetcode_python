from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        l = position[0]
        r = position[-1]
        n = len(position)
        m -= 2
        while l <= r:
            mid = (l + r) // 2
            count = 0
            left = 0
            for i in range(1, n):
                if position[-1] - position[i] < mid:
                    break
                if position[i] - position[left] >= mid:
                    left = i
                    count += 1
            if count >= m:
                l = mid + 1
            else:
                r = mid - 1
        return r
