class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd,even=1,0
        n=len(A)
        while odd<n:
            while odd<n and A[odd]%2==1:
                odd+=2
            while even<n and A[even]%2==0:
                even+=2
            if odd<n and even<n:
                A[odd],A[even]=A[even],A[odd]
        return A
