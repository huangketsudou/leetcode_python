from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        for timePoint in timePoints:
            times.append(int(timePoint[0:2]) * 60 + int(timePoint[3:5]))
        times.sort()
        result = 1440 - times[-1]+times[0]
        for i in range(1 ,len(times)):
            result = min(result,times[i]-times[i-1])
        return result