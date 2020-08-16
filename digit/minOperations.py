class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0
        start = 1
        end = 2 * (n - 1) + 1
        diff = end - start
        summary = 0
        while diff > 0:
            summary += diff
            diff -= 4
        return summary // 2
