from typing import List
from collections import deque


class Solution:
    # 解题思路
    # 确定矩形的最高点，并向下和向左扩展需按照最大的面积，该面积就是以i，j位置的矩形为起点的最大可能的矩形数量，
    # 不要用最大寻找最大矩形面积的形式做，需要考虑的情况太多了
    def numSubmat(self, mat: List[List[int]]) -> int:
        """

        :param mat:
        :return:
        """
        m, n = len(mat), len(mat[0])
        res = 0
        for i in range(m):
            tmp = [1] * n
            for j in range(i, m):
                for k in range(0, n):
                    tmp[k] &= mat[j][k]
                dp = tmp[:]
                for k in range(n):
                    if dp[k] == 1:
                        if k - 1 < 0:
                            dp[k] = 1
                        else:
                            dp[k] = dp[k-1]+1
                        res += dp[k]
        return res
