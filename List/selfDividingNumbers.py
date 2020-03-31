class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans=[]
        for i in range(left,right+1):
            if self.isselfdiv(i):
                ans.append(i)
        return ans

    def isselfdiv(self,number):
        left=number
        while left:
            left,digit=divmod(left,10)
            if digit==0 or number%digit!=0:
                return False
        return True
