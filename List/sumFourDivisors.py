class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def division(n):
            d=set()
            for i in range(1,int(math.sqrt(n))+1):
                if n%i==0:
                   d.add(i)
                   d.add(n//i)
                if len(d)>4:
                    return list(d)
            return list(d)
        s=0
        for num in nums:
            r=division(num)
            if len(r)==4:
                s+=sum(r)

        return s
        
        
class Solution:
#思路——质因数分解，但是对于立方数而言，也是符合条件的
    def sumFourDivisors(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            upper = nums[0]
        else:
            upper = max(*nums)
        # 首先在这里筛选素数
        isPrim = [True for _ in range(upper)]
        i = 2
        while i * i < upper:
            if isPrim[i]:
                j = i * i
                while j < upper:
                    isPrim[j] = False
                    j += i
            i += 1
        # 把素数都提取出来
        prims = [i for i in range(2, upper) if isPrim[i]]
        ans = 0
        for num in nums:
            for prim in prims:
                # 已经不可能了，后续不算了
                if prim * prim > num:
                    break
                # 立方数是符合的，这个比较坑，开始没想到，比如 8
                if prim * prim * prim == num:
                    ans += (1 + num + prim + prim * prim)
                    break
                # 可以分解成两个质数乘积！！！
                if num % prim == 0 and isPrim[num // prim] and prim * prim != num:
                    ans += (1 + num + prim + num // prim)
                    break
        return ans
