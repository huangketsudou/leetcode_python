class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        n=len(A)
        left,right=0,n-1
        ans=[0]*n
        i=n-1
        while left<=right:
            if A[left]**2<=A[right]**2:
                ans[i]=A[right]**2
                right-=1
            else:
                ans[i]=A[left]**2
                left+=1
            i-=1
        return ans

