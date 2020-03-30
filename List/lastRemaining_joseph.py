class Solution2:
    #编号从0开始
    '''
    递推公式，f(N,M)=(f(N-1,M)+m)%N
    将f(N,M)理解为最后一个被出队的人在N人中的序号，那么当f(N,M)号人被出队后，仅剩下的N-1人以f(N,M)+1为队头，重新排列，
    f(N-1,M)为N-1人时，最后一个出队的人在N-1人中的序号，则f(N-1,M)与f(N,M)的关系可以表示为
    f(N-1,M)=f(N,M)-M,则f(N,M)=f(N-1,M)+M,由于可能越界，所以f(N,M)=(f(N-1,M)+M)%N
    '''
    def lastRemaining(self, n: int, m: int) -> int:
        f=0
        for i in range(2,n+1):
            f=(f+m)%i
        return f

class Solution:
    #编号从1开始
    def lastRemaining(self, n: int, m: int) -> int:
        f=0
        for i in range(2,n+1):
            f=(f+m)%i
        return f+1 #仅修改了最后的结果输出


k=Solution()
print(k.lastRemaining(10,17))




# def f(n, m):
#     if n == 0:
#         return 0
#     x = f(n - 1, m)
#     return (m + x) % n
#
# class Solution:
#     def lastRemaining(self, n: int, m: int) -> int:
#         return f(n, m)
