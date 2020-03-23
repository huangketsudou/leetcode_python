class Solution:
    def findLHS(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        c = Counter(nums)
        k = sorted(list(c.keys()))
        res = 0
        for i in range(1, len(k)):
            if k[i] - k[i - 1] == 1:
                res = max(c[k[i]] + c[k[i - 1]], res)
        return res


class Solution2:
    def findLHS(self, nums: List[int]) -> int:
        m=dict()
        res=0
        for num in nums:
            m[num]=m.get(num,0)+1
            if num+1 in m:
                res=max(res,m[num]+m[num+1])
            if num-1 in m:
                res=max(res,m[num]+m[num-1])
        return res

k = Solution()
print(k.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
