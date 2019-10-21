from typing import List
import bisect


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        length=len(nums)
        if length<3:
            return 0
        substact = float('inf')
        # answer=0
        for i in range(length-2):
            L=i+1
            R=length-1
            while L<R:
                summary=nums[i]+nums[L]+nums[R]
                diff=summary-target
                if diff==0:
                    return target
                elif diff < 0:
                    L+=1
                    while L <R and nums[L]==nums[L-1]:
                        L+=1
                else:
                    R-=1
                    while L<R and nums[R]==nums[R+1]:
                        R-=1
                # if abs(diff)<substact:
                #     answer=summary
                #     substact=abs(diff)
                if abs(diff)<abs(substact-target):
                    substact=summary
        return substact


k=Solution()
print(k.threeSumClosest([-1,1,2,-4],1))
