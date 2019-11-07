from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        n=len(nums)
        nums.sort()
        tmp=[]
        used=[]
        self.core(n,answer,nums,tmp,used)
        return answer


    def core(self,n,answer,nums,tmp,used):
        if len(used)==n:
            answer.append(tmp[:])
        for i in range(n):
            if i in used:
                continue
            if i>0 and nums[i]==nums[i-1] and i-1 not in used:
                continue
            tmp.append(nums[i])
            used.append(i)
            self.core(n,answer,nums,tmp,used)
            used.pop(-1)
            tmp.pop(-1)



k=Solution()
print(k.permuteUnique([3,1,1]))
