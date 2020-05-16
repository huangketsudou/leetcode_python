from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        while i<n:
            while nums[i]!=i+1 and 0<nums[i]<=n and nums[i]!=nums[nums[i]-1]:
                # if nums[i]<=0 or nums[i]>n or nums[i]==nums[nums[i]-1]:
                #     break
                #确保先修改的是nums[nums[i]-1],而不会先对nums[i]造成修改
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
                #nums[i],nums[nums[i]-1]=nums[nums[i]-1],nums[i]
                #这句话是错的
            i+=1
        for i,num in enumerate(nums):
            if num!=i+1:
                return i+1
        return n+1

k=Solution()
print(k.firstMissingPositive([1,3,3]))

k.firstMissingPositive([1,1])
k.firstMissingPositive([3,4,-1,1])
