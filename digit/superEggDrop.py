class Solution:
    #我的考虑，结果是错的
    def superEggDrop(self, K: int, N: int) -> int:
        def core(down, up, left):
            if up<=down:return 1
            if left == 1:
                return up - down
            middle = (down + up) // 2 #并不是简单的二分就能得到结果的
            return max(core(down, middle - 1, left - 1), core(middle + 1, up, left)) + 1

        return core(1, N + 1, K)


class Solution2:
    def superEggDrop(self, K: int, N: int) -> int:
        memo={}
        def core(n,k):
            if (k,n) not in memo:
                if n==0:ans=0
                elif k==1:ans=1
                else:
                    lo,hi=1,n
                    while lo+1<hi:
                        x=(lo+hi)//2
                        t1=core(x-1,k-1)
                        t2=core(n-x,k)
                        if t1<t2:
                            lo=x
                        elif t1>t2:
                            hi=x
                        else:
                            lo=hi=x

                    ans=1+min(max(core(x-1,k-1),core(n-x,k)) for x in (lo,hi))
                memo[k,n]=ans
            return memo[k,n]
        return core(N,K)
k = Solution2()
print(k.superEggDrop(2,1))



class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # Right now, dp[i] represents dp(1, i)
        dp = list(range(N+1))
        dp2 = [0] * (N+1)
        for k in range(2, K+1):
            # Now, we will develop dp2[i] = dp(k, i)
            x = 1
            for n in range(1, N+1):
                # Let's find dp2[n] = dp(k, n)
                # Increase our optimal x while we can make our answer better.
                # Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
                # is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
                while x < n and max(dp[x-1], dp2[n-x]) >= max(dp[x], dp2[n-x-1]):
                    x += 1

                # The final answer happens at this x.
                dp2[n] = 1 + max(dp[x-1], dp2[n-x])

            dp = dp2[:]

        return dp[-1]


class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        if N == 1:
            return 1
        f = [[0] * (K + 1) for _ in range(N + 1)]
        for i in range(1, K + 1):
            f[1][i] = 1
        ans = -1
        for i in range(2, N + 1):
            for j in range(1, K + 1):
                f[i][j] = 1 + f[i - 1][j - 1] + f[i - 1][j]
            if f[i][K] >= N:
                ans = i
                break
        return ans

