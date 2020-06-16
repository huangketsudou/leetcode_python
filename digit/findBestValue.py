from typing import List


class Solution:
    # 排序之后，检查前缀和与目标的差值，除以剩下的数的个数值是否小于于当前的值，如果小了，就需要修改，其值需要判定是x或者x+1
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        summary = 0
        length = len(arr)
        for i, v in enumerate(arr):
            x = (target - summary) // (length - i)
            if v > x:
                t = (target - summary) / (length - i)
                if t - x > 0.5:
                    return x + 1
                else:
                    return x
            summary += v
        return arr[-1]


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        summary = sum(arr)
        if summary < target:
            return max(arr)
        length = len(arr)
        val = target // length
        summary, last = 0, 0
        while summary < target:
            last = summary
            summary = 0
            for i in range(length):
                summary += min(arr[i], val)
            val += 1
        return val - 2 if abs(target - summary) >= abs(target - last) else val - 1


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        summary = sum(arr)
        if summary < target:
            return max(arr)
        length = len(arr)
        left, right = target // length, min(target, arr[-1])
        while left < right:
            mid = (left + right) // 2
            summary = 0
            for i in range(length):
                summary += min(arr[i], mid)
            if target < summary:
                right = mid - 1
            else:
                left = mid + 1
        summary, summaryleft, summaryright = 0, 0, 0
        for v in arr:
            summary += min(v, left)
            summaryleft += min(v, left - 1)
            summaryright += min(v, left + 1)
        if abs(target - summaryright) >= abs(target - summary):
            return left if abs(target - summary) < abs(target - summaryleft) else left - 1
        else:
            return left + 1


import bisect


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            prefix.append(prefix[-1] + num)
        l, r, ans = 0, max(arr), -1
        while l <= r:
            mid = (l + r) // 2
            it = bisect.bisect_left(arr, mid)
            cur = prefix[it] + (n - it) * mid
            if cur <= target:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        def check(x):
            return sum(min(x, i) for i in arr)

        choosesmall = check(ans)
        choosebig = check(ans + 1)
        return ans if abs(choosesmall - target)<=abs(choosebig - target) else ans + 1
