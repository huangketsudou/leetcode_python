class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:return '0'
        sign=''
        if num<0:
            sign='-'
            num=-num
        res=''
        while num:
            num,mod=divmod(num,7)
            res=str(mod)+res
        return sign+res
