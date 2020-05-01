from typing import List


'''
给定一个长度为 n 的整数数组 A 。
假设 Bk 是数组 A 顺时针旋转 k 个位置后的数组，我们定义 A 的“旋转函数” F 为：
F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1]。
计算F(0), F(1), ..., F(n-1)中的最大值。
'''

'''
#https://leetcode-cn.com/problems/rotate-function/solution/c-cuo-wei-xiang-jian-fa-by-da-li-wang/
计算F(k)=0*Bk[0]+1*Bk[1]+...+(n-2)*Bk[n-2]+(n-1)*Bk[n-1]
计算F(k+1)=0*Bk[n-1]+1*Bk[0]+2*Bk[1]+...+(n-1)*Bk[n-2]
2式剪1式，F(k+1)-F(k)=(Bk[0]+Bk[1]+...+Bk[n-2])-(n-1)*Bk[n-1]
令F(k+1)-F(k)=(Bk[0]+Bk[1]+...+Bk[n-2]+Bk[n-1])-n*Bk[n-1],令S=Sum({Bk})
所以得到推导式：F(k+1)=F(k)+S-n*Bk[n-1]
注：Bk[n-1]是一个与k相关的值，表示经过旋转k次后的数组最后一个数
k=0：Bk[n-1]是A[n-1],k=1:Bk[n-1]=A[n-2],以此类推
'''


class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        n=len(A)
        S=0
        t=0
        for i,v in enumerate(A):
            S+=v
            t+=i*v
        res=t
        for j in range(n-1,-1,-1):
            t+=S-n*A[j]
            res=max(res,t)
        return res
