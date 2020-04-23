class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        seen={}
        n=len(s)
        # def core(string):
        #     n = len(string)
        #     if n == 0: return 1
        #     if string.startswith('0'): return 0
        #     count = 0
        #     for i in range(1, n + 1):
        #         if int(string[:i]) > k: return count % MOD
        #         tmp = core(string[i:])
        #         count += (tmp) % MOD
        #     return count % MOD
        #
        # ans = core(s)
        # return ans


        def helper(i):
            if i==n:return 1
            if s[i]=='0':return 0
            count=0
            for j in range(i+1,n+1):
                if int(s[i:j])>k:return count %MOD
                if (i,j) not in seen:
                    tmp=helper(j)
                    seen[(i,j)]=tmp % MOD
                count+=seen[(i,j)]
            return count % MOD
        ans=helper(0)
        return ans % MOD


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        f = [0]*(n+1)
        f[0] = 1 #对应上面的i==n
        m = len(str(k))
        MOD = 10**9+7
        #定义f数组为到某个数字的位置为止，其可行的排列组合有多少种
        for i in range(1, n+1):
            for j in range(1, m+1):#定义这里的m，可以避免出现c或者java里的溢出
                if i-j >= 0:
                    if s[i-j] != '0' and int(s[i-j:i]) <= k:#开头不为0，且数字小
                        f[i] += f[i-j]
                        f[i] %= MOD
        return f[n]

class Solution3:
    def numberOfArrays(self, s: str, k: int) -> int:
        n=len(s)
        m=len(str(k))
        dp=[0]*(n+1)
        dp[-1]=1
        MOD=10**9+7
        for i in range(n-1,-1,-1):
            for j in range(1,m+1):
                if i+j<=n:
                    if s[i]!='0' and int(s[i:i+j])<=k:
                        dp[i]+=dp[i+j]
                        dp[i] %= MOD
        return dp[0]

k=Solution3()
print(k.numberOfArrays("1234567890",90))