from typing import List

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        import sys
        sys.setrecursionlimit(10000000)
        import functools
        @functools.lru_cache(None)
        def c(a):
            if a == 0:
                return 1
            return a * c(a - 1)

        total = sum(balls)
        zong = c(total)
        for b in balls:
            zong //= c(b)

        cc = c(total // 2)
        import functools
        @functools.lru_cache(None)
        def dfs(pre, i, a, b, px, py):
            if i == len(balls):
                if pre == total / 2:
                    if a == b:
                        return cc / px * cc / py
                return 0
            res = 0
            for j in range(balls[i] + 1):
                if j == 0:
                    res += dfs(pre, i + 1, a, b + 1, px * c(j), py * c(balls[i] - j))
                elif j != balls[i]:
                    res += dfs(pre + j, i + 1, a + 1, b + 1, px * c(j), py * c(balls[i] - j))
                else:
                    res += dfs(pre + j, i + 1, a + 1, b, px * c(j), py * c(balls[i] - j))
            return res

        res = dfs(0, 0, 0, 0, 1, 1)
        return res / zong


class Solution(object):
    def getProbability(self, balls):
        """
        :type balls: List[int]
        :rtype: float
        """
        d = [1, 1]

        for i in range(2, 49):
            d.append(d[-1] * i)


        def cal(bs):
            tot = sum(bs)
            a = 1
            di = tot
            for num in bs:
                a *= (d[di] / d[di-num]) / d[num]
                di -= num
            return a


        dp = {}
        self.res = 0
        self.target = sum(balls) / 2
        all_d = {}
        for i,num in enumerate(balls):
            all_d[i] = num

        b2 = [[i,num] for i, num in enumerate(balls)]

        def dfs(cur, count1, cur_d):
            if not cur:
                if count1 == self.target:
                    c1 = {}
                    c2 = {}
                    for key in cur_d:
                        if cur_d[key]!=0:
                            c1[key] = cur_d[key]
                        if all_d[key]-cur_d[key]!=0:
                            c2[key] = all_d[key]-cur_d[key]
                    if len(c1)==len(c2):
                        #print c1,c2
                        self.res += cal([c1[key] for key in c1]) * cal([c2[key] for key in c2])
                return
            kind, count = cur[0]
            for nei in range(count+1):
                if count1 + nei <= self.target:
                    tmp = dict(cur_d)
                    tmp[kind] = nei
                    dfs(cur[1:], count1 + nei, tmp)
            return

        dfs(b2, 0, {})


        return 1.0 * self.res / cal(balls)