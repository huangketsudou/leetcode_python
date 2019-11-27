from typing import List



class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        answer=0
        m=len(s)
        n=len(t)
        def core(i,j):
            nonlocal answer
            if j==n:
                answer+=1
                return
            if m-i<n-j:return False
            for k in range(i,m):
                if s[k]==t[j]:
                    core(k+1,j+1)

        for i in range(m-n+1):
            if s[i]==t[0]:
                core(i+1,1)

        return answer

class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        m=len(s)
        n=len(t)
        dp=[[0]*(m+1) for _ in range(n+1)]
        dp[0][0]=1
        for i in range(1,n+1):
            for j in range(1,m+1):
                if t[i-1]==s[j-1]:
                    dp[i][j]=sum(dp[i-1][:j])
        return sum(dp[-1])


class Solution3:
    def numDistinct(self, s: str, t: str) -> int:
        n1 = len(s)
        n2 = len(t)
        dp = [[0] * (n1 + 1) for _ in range(n2 + 1)]
        for j in range(n1 + 1):
            dp[0][j] = 1
        for i in range(1, n2 + 1):
            for j in range(1, n1 + 1):
                if t[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        #print(dp)
        return dp[-1][-1]


k=Solution2()
print(k.numDistinct("aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe",
"bddabdcae"))
