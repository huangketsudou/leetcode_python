class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        ans = set()
        # 2**18 > bound
        for i in range(20):
            for j in range(20):
                v = x**i + y**j
                if v <= bound:
                    ans.add(v)
        return list(ans)

