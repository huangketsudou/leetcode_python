from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2: return []
        i = 0
        while i < n:
            while i+1!=nums[i]:
                if nums[nums[i]-1]==nums[i]:
                    break
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            i+=1
        res=[]
        for i,v in enumerate(nums):
            if i+1!=v:
                res.append(v)
        return res
