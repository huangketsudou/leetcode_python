from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        prevdiff=nums[1]-nums[0]
        count=2 if prevdiff!=0 else 1
        for i in range(2,n):
            diff=nums[i]-nums[i-1]
            if (diff > 0 and prevdiff <=0) or (diff<0 and prevdiff>=0):#必须记录下从第一个查开始的上一个差，否则无法判断
                count+=1
                prevdiff=diff
        return count


k = Solution()
print(k.wiggleMaxLength([1,1,7,4,9,2,5]))
