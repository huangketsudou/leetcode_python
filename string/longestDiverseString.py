class Solution:
    #实现思路：
    #任意时刻均添加当前存量最多的字母，而当最后两个字母相同时，从次最多的字母中选择
    #初始化存量，某一个字符的数量最多不超过其他两字符数量加一的两倍，即a=2(b+c+1),如aabaabaacaacaa
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        d = {'a':min(a,2*(b+c+1)),'b':min(b,2*(a+c+1)),'c':min(c,2*(b+a+1))}
        n = sum(d.values())
        res = []
        for i in range(n):
            cand = set(['a','b','c'])
            if len(res)>1 and res[-1]==res[-2]:
                cand.remove(res[-1])
            tmp = max(cand,key=lambda x:d[x])
            res.append(tmp)
            d[tmp] -= 1
        return ''.join(res)

