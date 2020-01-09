from typing import List


class Solution:
    # O(n)
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums: return 0
        currentsum = 0
        start= -1
        answer = float('inf')
        for i in range(len(nums)):
            currentsum += nums[i]
            while currentsum >= s:
                answer = min(i - start, answer)
                start += 1
                currentsum -= nums[start]
        return answer if answer != float('inf') else 0


class Solution2:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums : return 0
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        if nums[-1] < s: return 0
        import bisect
        res = float("inf")
        nums = [0] + nums
        for i in range(1, len(nums)):
            if nums[i] - s >= 0:
                loc = bisect.bisect_left(nums, nums[i] - s)
                if nums[i] - nums[loc] >= s:
                    res = min(res, i - loc)
                    continue
                if loc > 0:
                    res = min(res, i - loc + 1)
        return res




class Solution3:
    # O(n)
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        summary = [0] * (n + 1)
        for i in range(1, n + 1):
            summary[i] = nums[i - 1] + summary[i - 1]
        answer = float('inf')
        start = 0
        for i in range(1, n + 1):
            while summary[i] - summary[start] >= s:
                answer = min(answer, i - start)
                start += 1
        return answer if answer != float('inf') else 0


k = Solution()
print(k.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
