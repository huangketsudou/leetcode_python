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




class Solution:
    #允许元素重复两次
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:return -1
        slow=0
        fast=1
        count=1
        while fast<n:
            if nums[fast]==nums[slow] and count<2:
                slow+=1
                nums[slow],nums[fast]=nums[fast],nums[slow]
                fast+=1
                count+=1
            elif nums[fast]==nums[slow] and count==2:
                fast+=1
            else:
                slow+=1
                nums[slow],nums[fast]=nums[fast],nums[slow]
                fast+=1
                count=1
        return slow+1
    
k=Solution()
a=[1,1,1,1,1,1,1,1,3]
print(k.removeDuplicates(a))
print(a)
