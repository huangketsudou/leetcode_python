def negative(n):
    return add(~n,1)


def substract(m,n):
    #add(~n,1)，求-n补码
    return add(m,negative(n))


def getTrueBit(n):
    return bin(-5 & 0xffffffff)

def add(a, b):
        while(b):
           a,b = (a^b) & 0xFFFFFFFF,((a&b)<<1) & 0xFFFFFFFF
        return a if a<=0x7FFFFFFF else ~(a^0xFFFFFFFF)


def getsign(n):
    return n>>31


def myabs(n):
    return negative(n) if n>>31 else n


def multiply(m,n):
    flag=True
    if getsign(m)==getsign(n):
        flag=False
    m=myabs(m)
    n=myabs(n)
    ans=0
    while n:
        #小学的长乘法
        if n & 1:
            ans=add(ans,m)
        m=m<<1
        n=n>>1
    if flag:
        ans=negative(ans)
    return ans


def divide(m,n,p=False):
    #p确定是否用python的表示方法来求余数，默认C++
    sign=True if getsign(m) ^ getsign(n) else False
    signofm=True if getsign(m) else False
    signofn=True if getsign(n) else False
    m=myabs(m)
    n=myabs(n)
    count=0
    while m>=n:
        count+=1
        n<<=1
    result=0
    while count:
        count-=1
        n>>=1
        if m>=n:
            #求商
            result=add(result,1<<count)
            m=substract(m,n)
    if sign:
        result=negative(result)
    if p:
        if sign:
            m=substract(n,m)
        if signofn:
            return result,negative(m)
        return result,m
    else:
        #C++情况下
        if signofm:
            return result,negative(m)
        return result,m
