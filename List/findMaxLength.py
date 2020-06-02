from collections import defaultdict


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mapping = defaultdict(int)
        maxlength = 0
        sum = 0
        mapping[0]=-1
        for i in range(len(nums)):
            sum = sum + (1 if nums[i] == 0 else -1)
            if sum in mapping:
                maxlength = max(maxlength,i - mapping[sum])
            else:
                mapping[sum] = i
        return maxlength