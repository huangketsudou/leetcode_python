from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n < 2: return 0
        intervals.sort(key=lambda x: x[0])
        dp = [0] * n
        dp[0] = 1
        ans = 1
        for i in range(1, n):
            maximun = 0
            for j in range(i - 1, -1, -1):
                if not intervals[i][0] < intervals[j][1]:
                    maximun = max(dp[j], maximun)
            dp[i] = maximun + 1
            ans = max(ans, dp[i])
        return n - ans


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n < 2: return 0
        intervals.sort(key=lambda x: x[1])
        dp = [0] * n
        dp[0] = 1
        ans = 1
        for i in range(1, n):
            maximun = 0
            for j in range(i - 1, -1, -1):
                if not intervals[i][0] < intervals[j][1]:
                    maximun = max(dp[j], maximun)
                    break
            dp[i] = max(maximun + 1, dp[i - 1])
            ans = max(ans, dp[i])
        return n - ans


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals = sorted(intervals, key=lambda x: x[1])

        ans = 0
        end = -float('inf')  # 结束时间
        for i in intervals:
            if i[0] >= end:
                ans += 1
                end = i[1]
        return len(intervals) - ans


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n < 2: return 0
        intervals.sort(key=lambda x: x[0])
        end = intervals[0][1]
        prev = 0
        count = 0
        for i in range(1, n):
            if intervals[prev][1] > intervals[i][0]:
                if intervals[prev][1] > intervals[i][1]:
                    prev = i
                count += 1
            else:
                prev = i
        return count
