class Solution:
    def binaryGap(self, N: int) -> int:
        strN=bin(N)[2:]
        n=len(strN)
        i=n-1
        while i>=0:
            if strN[i]=='1':
                break
            i-=1
        if i<=0:return 0
        j=i-1
        ans=0
        while j>=0:
            if strN[j]=='1':
                ans=max(ans,i-j)
                i=j
            j-=1
        return ans
k=Solution()
print(k.binaryGap(0))
