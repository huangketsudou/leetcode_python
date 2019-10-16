class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        strx=str(x)
        if strx==strx[::-1]:
            return True
        return False

class Solution2:
    def isPalindrome(self,x):
        if x<0 or (x%10==0 and x!=0):
            return False
        y=0
        while y<x:
            pop=x%10
            y=y*10+pop
            x//=10
        return x==y or x//10==y
    
    
k=Solution()
k.isPalindrome(123)
