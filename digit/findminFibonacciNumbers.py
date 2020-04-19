class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        f1, f2 = 1, 1
        fib=[1,1]
        while f2<k:
            f=f1+f2
            f1,f2=f2,f
            fib.append(f)

        ans=0
        while k:
            while fib[-1]>k:
                fib.pop()
            k-=fib[-1]
            ans+=1
        return ans
