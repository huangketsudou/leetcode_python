from typing import List
import functools


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        reverse_nums = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1 #遇到0，乘以1,连乘连加常用的方法
            reverse_nums[i] *= reverse_nums[i - 1] or 1
        return max(nums + reverse_nums)



class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        pre_max = nums[0]
        pre_min = nums[0]
        for num in nums[1:]:
            cur_max = max(pre_max * num, pre_min * num, num)
            cur_min = min(pre_max * num, pre_min * num, num)
            res = max(res, cur_max)
            pre_max = cur_max
            pre_min = cur_min
        return res


class Solution3:
    def maxProduct(self, nums: List[int]) -> int:
        # 目前的累乘
        cur_pro = 1
        # 前面最小的正数
        min_pos = 1
        # 前面最大的负数
        max_neg = float("-inf")
        # 结果
        res = float("-inf")
        for num in nums:
            cur_pro *= num
            # 考虑三种情况
            # 大于0
            if cur_pro > 0:
                res = max(res, cur_pro // min_pos)
                min_pos = min(min_pos, cur_pro)
            # 小于0
            elif cur_pro < 0:
                if max_neg != float("-inf"):
                    res = max(res, cur_pro // max_neg)
                else:
                    res = max(res, num)
                max_neg = max(max_neg, cur_pro)
            # 等于0
            else:
                cur_pro = 1
                min_pos = 1
                max_neg = float("-inf")
                res = max(res, num)
        return res


k=Solution()
print(k.maxProduct([2,3,4,5,6,0,7]))
