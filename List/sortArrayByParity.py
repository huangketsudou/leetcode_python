class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        n = len(A)
        left, right = 0, n - 1
        while left<right:
            while left<n and A[left]%2==0:
                left+=1
            while right>=0 and A[right]%2==1:
                right-=1
            if left<right:
                A[left],A[right]=A[right],A[left]
        return A
