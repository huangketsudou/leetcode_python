#要求使用O(1)空间
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            while nums[i]!=i+1:
                if nums[nums[i]-1]==nums[i]:
                    break
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        res=[]
        for i in range(n):
            if nums[i]!=i+1:
                res.append(i+1)
        return res
