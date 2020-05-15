from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mapping=defaultdict(int)
        mapping[0]=1
        prev=0
        ans=0
        for i in range(len(nums)):
            prev+=nums[i]
            ans+=mapping[prev-k]
            mapping[prev]+=1
        return

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=0
        for i in range(n):
            prev=0
            for j in range(i,n):
                prev+=nums[j]
                if prev==k:
                    ans+=1
        return ans
