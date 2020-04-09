class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n=len(name)
        m=len(typed)
        def core(i,j):
            if i==n and j==m:
                return True
            if i==n or j==m:
                return False
            if name[i]==typed[j]:
                return core(i,j+1) or core(i+1,j+1)
            return False
        return core(0,0)

k=Solution()
print(k.isLongPressedName(name = "alex", typed = "aaleex"))


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n,m=len(name),len(typed)
        dp=[[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(i,m):
                if i==0 and j==0:
                    dp[i][j]=name[i]==typed[j]
                elif i==0:
                    dp[i][j]=dp[i][j-1] and name[i]==typed[j]
                else:
                    dp[i][j]=(dp[i][j-1] or dp[i-1][j-1]) and name[i]==typed[j]
        return dp[-1][-1]


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n,m=len(name),len(typed)
        left=0
        for c in typed:
            if name[left]==c:
                left+=1
            if left==n:
                return True
        return False
