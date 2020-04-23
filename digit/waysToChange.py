class Solution:
    # i表示利用前i种硬币能够成结果v的方案数，所以状态转移方程可以表示为
    # f(i,v)=sum(f(i-1,v-j*ci)).ci为第i种硬币币值，j=[0,v//ci]
    # 简化上文的求和公式，展开得到，f(i,v)=f(i-1,v)+f(i-1,v-ci)+f(i-1,v-2ci)+....
    # 而f(i,v-ci)=f(i-1,v-ci)+f(i-1,v-2ci)+...
    # 所以最后的求和公式可以简化为f(i,v)=f(i-1,v)+f(i,v-ci)
    # 因为我们只关心i-1与i所以最终可简化到只有一个数组的形式
    def waysToChange(self, n: int) -> int:
        # 每次限定能够使用的硬币
        MOD=10**9+7
        dp = [1] * (n + 1)
        coin = [1, 5, 10, 25]
        for i in range(1, 4):
            for j in range(n + 1):
                if j - coin[i] >= 0:
                    dp[j] = (dp[j] + dp[j - coin[i]])%MOD
        return dp[-1]% MOD


class Solution2:
    def waysToChange(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(4)]
        for k in range(n + 1):
            dp[0][k] = 1
        coin = [1, 5, 10, 25]
        for i in range(1, 4):
            for j in range(n + 1):
                for g in range(j // coin[i] + 1):
                    dp[i][j] += dp[i - 1][j - g * coin[i]]
        if n < 5:
            id = 0
        elif n < 10:
            id = 1
        elif n < 15:
            id = 2
        else:
            id = 3
        return dp[id][n]


class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 10**9 + 7
        '''
        对于给定的n，先枚举25分硬币的数量个数i，余下的部分记为r=n-25*i，将r表示为r=10*a+5*b+c
        这里的a能取到的最大值为a0=(r-(r mod 10))//10,当a=a0时限定c<5可以得到b的最大值为b0，所以c0=r-10*a0-5*b0，
        考虑选择i个25分硬币，假设选择x个10分硬币，那么还剩下的金额可以表示为10*(a0-x)+5*b0+c0
        考虑把10*(a0-x)这一项全部用5分硬币来替换，上面的式子也可以写为5*(2a0-2x-b0)+c0,那么5分硬币的选择范围就是
        [0,2a0-2x+b0],剩下的用1分硬币补齐，也就是说25分硬币选i个，10分硬币选x个时的方案数为2a0-2x+b0+1,对x求和可得
        sum((2a0-2x+b0+1)),其中x=[0,a0]，化简得到(a0+1)*(a0+b0+1)
        '''
        ans = 0
        for i in range(n // 25 + 1):
            rest = n - i * 25
            a, b = rest // 10, rest % 10 // 5
            ans += (a + 1) * (a + b + 1)
        return ans % mod



k = Solution2()
print(k.waysToChange(25))
