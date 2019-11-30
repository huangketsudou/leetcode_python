from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:return 0
        nums.sort()
        n=len(nums)
        maxlength=1
        currentlength=1
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                if nums[i]==nums[i-1]+1:
                    currentlength+=1

                else:
                    maxlength = max(maxlength, currentlength)
                    currentlength=1

        return max(maxlength, currentlength)

class Solution2:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                #寻找起点数字
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak



k=Solution()
print(k.longestConsecutive([1,2,1,0]))
