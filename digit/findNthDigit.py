class Solution:
    def findNthDigit(self, n: int) -> int:
        base = 9
        cursum = base
        presum = 0
        for i in range(1,100000):
            if n <= cursum:
                div, mod = divmod(n - presum - 1, i)
                num = 10 ** (i - 1) + div
                return int(str(num)[mod])
            base = (10 ** (i)) * (i + 1) * 9
            presum = cursum
            cursum += base
