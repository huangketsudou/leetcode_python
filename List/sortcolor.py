from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        point0,point1,point2=0,n-1,n-1
        while point1>=point0:
            if nums[point1]==0:
                nums[point0],nums[point1]=nums[point1],nums[point0]
                point0+=1
            elif nums[point1]==2:
                nums[point2],nums[point1]=nums[point1],nums[point2]
                point2-=1
                point1-=1
            else:
                point1-=1
            print(point1)


k=Solution()
a=[0,0,2,1,1,0]
k.sortColors(a)
print(a)
