class Solution:
    def guessNumber(self, n: int) -> int:
        left=0
        right=n
        while left<=right:
            midlle=(left+right)//2
            if guess(midlle)==0:
                return midlle
            elif guess(midlle)>0:
                left=midlle+1
            else:
                right=midlle-1
