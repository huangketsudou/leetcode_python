class Solution:
    '''
    对于两个具有相同位数的数字，其相对大小取决于从左到右第一位不同的数之间的大小
    如1axxxx,1bxxx,两者的大小取决于a和b的大小，因此数据的删除顺序是从左到右的
    '''
    def removeKdigits(self, num: str, k: int) -> str:

        n=len(num)
        if n==k:return '0'
        numstack=[]
        for digit in num:
            while k and numstack and numstack[-1]>digit:
                numstack.pop()
                k-=1
            numstack.append(digit)
        finalstack=numstack[:-k] if k else numstack #栈中的数据全是递增的，而k还没有减到0
        #例如数据：1234567，对这种情况，删除尾部的数据就可以了
        return ''.join(finalstack).lstrip('0') or '0'
