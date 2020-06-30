class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start+2*i for i in range(n)]
        prev = 0
        for j in nums:
            prev^=j
        return prev