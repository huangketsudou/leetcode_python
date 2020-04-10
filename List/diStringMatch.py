class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        ans=[]
        n=len(S)
        i,left,right=0,0,n
        while i<n:
            if S[i]=='I':
                ans.append(left)
                left+=1
            else:
                ans.append(right)
                right-=1
            i+=1
        ans.append(left)
        return ans
