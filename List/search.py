from typing import List



class Solution:
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

k=Solution()
print(k.search([5,5,6,1,2,3],4))
