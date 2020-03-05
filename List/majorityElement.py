from typing import List
#元素占一半以上
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        candidate=None
        for num in nums:
            if count==0:
                candidate=num
            count+=(1 if num==candidate else -1)
        return candidate
        
#摩尔投票法-https://blog.csdn.net/u014248127/article/details/79230221     
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2+1]
        
        
        
        if len(nums) <= 1: return nums
        candidate1, count1 = None, 0
        candidate2, count2 = None, 0
        result = []
        for i in nums:
            if i == candidate1:
                count1 += 1
            elif i == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = i
                count1 = 1
            elif count2 == 0:
                candidate2 = i
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        count1 = count2 = 0
        for i in nums:
            if candidate1 == i:
                count1 += 1
            if candidate2 == i:
                count2 += 1
        if count1 > len(nums) // 3:
            result.append(candidate1)
        if count2 > len(nums) // 3:
            result.append(candidate2)
        return result
