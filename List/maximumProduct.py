class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        res=max(nums[0]*nums[1]*nums[2],nums[-1]*nums[0]*nums[1])
        return res

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        _inf = float('inf')
        max1, max2, max3, min1, min2 = -_inf, -_inf, -_inf, _inf, _inf
        for num in nums:
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        return max(max1 * max2 * max3, max1 * min1 * min2)


k=Solution()
print(k.maximumProduct([-1,-7,1,2,3,4]))
