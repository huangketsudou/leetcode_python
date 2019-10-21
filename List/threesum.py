class Solution:
    def threeSum(self, nums):
        length = len(nums)
        if length < 3:
            return []
        all = []
        nums.sort()
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue
            L = i + 1
            R = length - 1
            while L < R:
                summary = nums[i] + nums[L] + nums[R]
                if summary == 0:
                    all.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L + 1]: L += 1
                    while L < R and nums[R] == nums[R - 1]: R -= 1
                    L += 1
                    R -= 1
                elif summary > 0:
                    R -= 1
                else:
                    L += 1
        return all


from typing import List
import bisect


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        counts = {}
        for i in nums:
            counts[i] = counts.get(i, 0) + 1
        nums = sorted(counts)
        for i, num in enumerate(nums):
            if counts[num] > 1:
                if num == 0:
                    if counts[num] > 2:
                        ans.append([0, 0, 0])
                else:
                    if -num*2 in nums:
                        ans.append([num, num, -2*num])
            if num < 0:
                twosum = -num
                left = bisect.bisect_left(nums, (twosum-nums[-1]), i+1)
                for i in nums[left:bisect.bisect_right(nums, (twosum//2), left)]:
                    j = twosum-i
                    if j in counts and j != i:
                        ans.append([num, i, j])
        return ans

k = Solution()
print(k.threeSum([-1,-1, -2, 3, 4]))
