from typing import List


class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        i = n - 1
        j = m - 1
        set1 = set(nums1)
        set2 = set(nums2)
        common = set1 & set2
        print(common)
        prev1 = 0
        prev2 = 0
        while i >= 0 and j >= 0:
            while i >= 0 and nums1[i] not in common:
                prev1 += nums1[i]
                i -= 1
            while j >= 0 and nums2[j] not in common:
                prev2 += nums2[j]
                j -= 1
            if nums1[i] == nums2[j]:
                MAX = max(prev1, prev2) + nums2[j]
                prev1 = prev2 = MAX
            i -= 1
            j -= 1
        while i >= 0:
            prev1 += nums1[i]
            i -= 1
        while j >= 0:
            prev2 += nums2[j]
            j -= 1
        return max(prev1, prev2) % (10**9+7)

k=Solution()
print(k.maxSum(nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]))