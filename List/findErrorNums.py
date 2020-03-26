class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tmp = 0
        for i in range(1, n + 1):
            tmp = tmp ^ i ^ nums[i - 1]
        diff = tmp & ~(tmp - 1)
        xor1 = xor2 = 0
        for i in nums:
            if (i & diff) != 0:
                xor1 ^= i
            else:
                xor2 ^= i
        for i in range(1, n + 1):
            if (i & diff) != 0:
                xor1 ^= i
            else:
                xor2 ^= i
        for i in range(n):
            if nums[i] == xor2:
                return [xor2, xor1]
        return [xor1, xor2]


class Solution2:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        tmp = 0
        for i in range(1, n + 1):
            tmp = tmp ^ i ^ nums[i - 1]
        diff = tmp & (-tmp)
        x = 0
        for i in range(1, n + 1):
            if diff & i:
                x ^= i
            if diff & nums[i - 1]:
                x ^= nums[i - 1]
        for n in nums:
            if n == x:
                return [x, tmp ^ x]
        return [tmp ^ x, x]


class Solution3:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c=Counter(nums)
        n=len(nums)
        missing=dup=0
        for i in range(1,n+1):
            if i not in c:
                missing=i
                continue
            c[i]-=1
            if c[i]>0:
                dup=i
        return [dup,missing]


l = Solution3()
print(l.findErrorNums([1, 2, 4, 4]))
