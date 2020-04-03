class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        n=len(S)
        start=0
        ans=[]
        for i in range(1,n+1):
            if i==n:
                if i - start >= 3:
                    ans.append([start, i - 1])
                break
            if S[start]!=S[i]:
                if i-start>=3:
                    ans.append([start,i-1])
                start=i
        return ans
