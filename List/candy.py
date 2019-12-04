from typing import List


class Solution2:
    def candy(self, ratings: List[int]) -> int:
        res = 1
        # 先前值
        pre = 1
        # 递减长度
        des_num = 0
        for i in range(1, len(ratings)):
            if ratings[i] >= ratings[i - 1]:
                if des_num > 0:
                    # 求和公式
                    res += ((1 + des_num) * des_num) // 2
                    # 递减长度比先前值大,所以我们要把先前值补充
                    if pre <= des_num: res += (des_num - pre + 1)
                    pre = 1
                    des_num = 0
                if ratings[i] == ratings[i - 1]:
                    pre = 1
                else:
                    pre += 1
                res += pre
            else:
                des_num += 1
        # print(des_num)
        if des_num > 0:
            res += ((1 + des_num) * des_num) // 2
            if pre <= des_num: res += (des_num - pre + 1)
        return res

class Solution3:
    def candy(self, ratings) -> int:
        n = len(ratings)
        if n == 0: return 0
        left_to_right = [1] * n
        right_to_left = [1] * n
        # 找从左到右满足条件的
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                # 保证从左到右的最少个数
                left_to_right[i] = left_to_right[i - 1] + 1
        # print(left_to_right)
        # 找从右到左满足条件的(同时要符合从左到右)
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                # 保证从左到右也满足, 同时也满足从右到左
                right_to_left[i] = max(left_to_right[i], right_to_left[i + 1] + 1)
        # print(right_to_left)
        res = 0
        # 选这个位置最大值
        for i in range(n):
            res += max(left_to_right[i], right_to_left[i])
        return res




k = Solution()
print(k.candy([1, 3, 4, 5, 2]))
