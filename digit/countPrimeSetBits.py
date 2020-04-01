class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        prime = [2, 3, 5, 7, 11, 13, 17, 19]
        ans=0
        for i in range(L,R+1):
            if self.isPrimeSet(i) in prime:
                ans+=1
        return ans


    def isPrimeSet(self, number):
        ans = 0
        while number:
            if number & 1:
                ans += 1
            number >>= 1
        return ans

class Solution(object):
    def countPrimeSetBits(self, L, R):
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(bin(x).count('1') in primes
                   for x in range(L, R+1))




k=Solution()
print(k.countPrimeSetBits(6,10))
