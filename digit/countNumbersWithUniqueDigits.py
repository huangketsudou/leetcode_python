class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        choice = 9
        ans = 10
        if n == 1: return ans
        tmp = 9
        for i in range(2, n + 1):
            tmp *= max(0, choice)
            choice -= 1
            ans += tmp
        return ans
