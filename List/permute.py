from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        n=len(nums)
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
            tmp.append(nums[i])
            used.append(i)
            self.core(n,answer,nums,tmp,used)
            used.pop(-1)
            tmp.pop(-1)


k=Solution()
print(k.permute([1,2,3]))
