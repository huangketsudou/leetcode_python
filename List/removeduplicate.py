from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return -1
        slow=0
        fast=1
        while fast<len(nums):
            if nums[fast]==nums[slow]:
                fast+=1
            else:
                slow+=1
                nums[slow],nums[fast]=nums[fast],nums[slow]
                fast+=1
        return slow+1


class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        while j < len(nums):
            temp = nums[j]
            while j < len(nums) and nums[j] == temp:
                j += 1
            nums[i] = temp
            i += 1
        print(nums)
        return i


k=Solution2()
print(k.removeDuplicates([0,0,1]))
