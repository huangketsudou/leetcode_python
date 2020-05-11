from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        import bisect
        res = []
        loc = []
        for idx, val in enumerate(intervals):
            loc.append([val[0], idx])
        loc.sort()
        for _, right in intervals:
            l = bisect.bisect_left(loc, [right])
            if l >= len(loc):
                res.append(-1)
            else:
                res.append(loc[l][1])
        return res


class Solution:
    #https://leetcode-cn.com/problems/find-right-interval/solution/xun-zhao-you-qu-jian-by-leetcode/
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        intervals = [tuple(interval) for interval in intervals]
        res = [-1] * n
        loc = {}
        for idx, val in enumerate(intervals):
            loc[val] = idx
        left_sort = sorted(intervals)
        right_sort = sorted(intervals, key=lambda x: x[1])
        i = 0
        j = 0
        # print(left_sort, right_sort)
        while i < n:
            while j < n and right_sort[j][1] <= left_sort[i][0]:
                res[loc[right_sort[j]]] = loc[left_sort[i]]
                j += 1
            else:
                i += 1
        return res

