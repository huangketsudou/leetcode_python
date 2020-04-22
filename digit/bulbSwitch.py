class Solution:
    def bulbSwitch(self, n: int) -> int:
        #对于这道题，分析可以知道，对于某一个数k，只有当前i是他的因数时，其状态才会改变，
        #当状态改变为偶数次时，灯关闭，奇数时灯打开
        #而数字的因素总是会成对出现，仅有完全平方数会出现奇数个因数
        return self.mysqrt(n)

    def mysqrt(self,n):
        #牛顿法求解平方根
        #求解f(x)=x^2==num,就是求解x^2-num==0的解，由倒数的定义知f'(x)=(f(x)-f(x0))/(x-x0)
        #可以得到x0~x-f(x)/f'(x),所以递推的可以得到近似解表达式为
        #对于一般的表达式，f(x)=x^m-a,f'(x)=mx^m-1
        #所以近似解的递推表达式为xn+1=xn-(xn^m-a)/(m*xn^(m-1))=(1-1/m)*xn+axn/(m*xn^m)
        #把2代入，得到xn+1=1/2*(xn+n/xn)
        a=n
        while a*a>n:
            a=(a+n//a)//2
        return a
