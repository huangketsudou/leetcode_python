class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        nxt = 0
        candy = 0
        while candies:
            candy += 1
            nxt %= num_people
            if candies>=candy:
                candies -= candy
                res[nxt] += candy
            else:
                res[nxt]+=candies
                candies=0
            nxt += 1
        return res


k=Solution()
print(k.distributeCandies(candies = 7, num_people = 4))


class Solution:
    #https: // leetcode - cn.com / problems / distribute - candies - to - people / solution / fen - tang - guo - ii - by - leetcode - solution /
    #等差数列求和得到需要分发的次数，如果发布完整还剩几个remaining，分析每一个人的构成方式
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people
        # how many people received complete gifts
        p = int((2 * candies + 0.25) ** 0.5 - 0.5)
        remaining = int(candies - (p + 1) * p * 0.5)
        rows, cols = p // n, p % n

        d = [0] * n
        for i in range(n):
            # complete rows
            d[i] = (i + 1) * rows + int(rows * (rows - 1) * 0.5) * n
            # cols in the last row
            if i < cols:
                d[i] += i + 1 + rows * n
        # remaining candies
        d[cols] += remaining
        return d
