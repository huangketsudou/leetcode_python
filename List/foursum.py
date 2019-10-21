from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length=len(nums)
        answer=[]
        if length<4:
            return answer
        nums.sort()
        for i in range(length-3):
            if i>0 and nums[i]==nums[i-1]:continue
            if sum(nums[i:i+4])>target:break
            if nums[i]+sum(nums[-3:])<target:continue
            for j in range(i+1,length-2):
                if j>i+1 and nums[j]==nums[j-1]:continue
                if sum(nums[j:j+3])+nums[i]>target:break
                if nums[i]+nums[j]+sum(nums[-2:])<target:continue
                L=j+1
                R=length-1
                while L<R:
                    summary=nums[i]+nums[j]+nums[L]+nums[R]
                    if summary==target:
                        answer.append([nums[i],nums[j],nums[L],nums[R]])
                        while L < R and nums[L] == nums[L + 1]: L += 1
                        while L < R and nums[R] == nums[R - 1]: R -= 1
                        L+=1
                        R-=1
                    elif summary<target:
                        L+=1
                        while L<R and nums[L]==nums[L-1]:
                            L+=1
                    else:
                        R-=1
                        while L<R and nums[R]==nums[R+1]:
                            R-=1
        return answer

k=Solution()
print(k.fourSum([1,0,-1,0,-2,2],0))
