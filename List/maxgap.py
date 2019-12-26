from typing import List
import functools
import math


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        max_num = max(nums)
        min_num = min(nums)
        gap = math.ceil((max_num - min_num) / (n - 1))
        bucket = [[float("inf"), float("-inf")] for _ in range(n - 1)]
        print(bucket)
        # 求出每个桶的最大值，和最小值
        for num in nums:
            if num == max_num or num == min_num:
                continue
            loc = (num - min_num) // gap
            bucket[loc][0] = min(num, bucket[loc][0])
            bucket[loc][1] = max(num, bucket[loc][1])
        print(bucket)
        # 遍历整个桶
        preMin = min_num
        res = float("-inf")
        for x, y in bucket:
            if x == float("inf"):
                continue
            res = max(res, x - preMin)
            preMin = y
        res = max(res, max_num - preMin)
        return res


class Solution2:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        min_num = min(nums)
        max_num = max(nums)
        bucketsize = max(1, (max_num - min_num) // (n - 1))
        print(bucketsize)
        bucketnum = (max_num - min_num) // bucketsize + 1
        buckets = [[float('inf'),float('-inf')] for _ in range(bucketnum)]
        for num in nums:
            id=(num-min_num)//bucketsize
            buckets[id][0]=min(num,buckets[id][0])
            buckets[id][1]=max(num,buckets[id][1])
        print(buckets)
        premax,gap=min_num,0
        for bucket in buckets:
            x,y=bucket
            if x==float('inf'):
                continue
            gap=max(gap,y-premax)
            premax=y
        return gap



k = Solution2()
print(k.maximumGap([3, 6, 9, 1]))
