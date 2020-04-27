from typing import List



class Solution:
    #元素不重复
    def search(self, nums: List[int], target: int) -> int:
        # 判断target值是在[左边界, 中值]区间还是[右边界, 中值]区间
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2

        while left <= right:
            # print(left, right, mid)
            if nums[mid] == target:
                return mid
            judge1 = nums[left] < nums[mid] and target < nums[mid] and target >= nums[left]  # 左半边有序
            judge2 = nums[left] > nums[mid] and (target < nums[mid] or target >= nums[left])  # 左半边旋转

            if judge1 or judge2:  # target在左半边
                right = mid - 1
                mid = (left + right) // 2
            else:  # target在右半边
                left = mid + 1
                mid = (left + right) // 2

        return -1

class Solution:
    #常规做法，
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>=nums[left]:#注意这里的等号是需要的
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1


k=Solution()
print(k.search([5,5,6,1,2,3],4))



class Solution:
    #元素可重复
    def search(self, nums: List[int], target: int) -> bool:
        n=len(nums)
        if n==0:return False
        left,right=0,n-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:return True
            if nums[mid]==nums[left]==nums[right]:
                right-=1
                left+=1
            elif nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return False


k=Solution()
print(k.search([2,5,6,0,0,1,2],2))
