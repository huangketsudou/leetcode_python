class Solution:
    def reverse(self,x:int) -> int:
        maxleft=(2**31)//10
        negative=False
        if x<0:
            negative=True
        absx=abs(x)
        rev=0
        while absx:
            pop=absx % 10
            absx//=10
            if rev>maxleft or (rev==maxleft and pop>7 and not negative):return 0
            if rev>maxleft or (rev==maxleft and pop>8 and negative):return 0
            rev=rev*10+pop
        if negative:
            rev=-rev
        return rev

k=Solution()
print(k.reverse(-12315333321))
