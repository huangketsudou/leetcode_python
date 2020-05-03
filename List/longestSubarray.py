from typing import List
import bisect

class Solution:
    '''
    i保留数组左边界
    st是一个递增的数组，只要保证最小值减最大值的绝对值小于st就可以确保st中的元素差小于limit
    '''
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        i = j = 0
        st = []
        ans = 0
        while j < len(nums):
            bisect.insort(st, nums[j])
            while st[-1] - st[0] > limit:
                st.remove(nums[i])
                i += 1
            j += 1
            ans = max(ans, len(st))
        return ans



k = Solution()
print(k.longestSubarray(nums=[4, 8, 5, 1, 7, 9], limit=6))
