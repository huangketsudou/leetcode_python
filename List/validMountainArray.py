class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n=len(A)
        if n<3:return False
        i=1
        while i<n:
            if A[i]<=A[i-1]:
                break
            i+=1
        if i==n or i==1:return False #考虑边界条件
        while i<n:
            if A[i]>=A[i-1]:
                break
            i+=1
        return i==n
    
