from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        m=len(primes)
        idx=[0]*m
        uglies=[0]*n
        uglies[0]=1
        for i in range(1,n):
            uglies[i]=min(x*uglies[y] for x,y in zip(primes,idx))
            for j in range(m):
                if uglies[i]>=primes[j]*uglies[idx[j]]:
                    idx[j]+=1
        return uglies[-1]

k=Solution()
print(k.nthSuperUglyNumber(12,[2,7,13,19]))