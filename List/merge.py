from typing import List


class Solution:
    #从前面开始跑
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
            return
        if n == 0:
            return

        for i in range(m - 1, -1, -1):
            nums1[i], nums1[i - m] = nums1[i - m], nums1[i]
        count = 0
        i = len(nums1)-m
        while i < len(nums1) or nums2:
            print(count)
            if i < len(nums1) and nums2:
                if nums1[i] <= nums2[0]:
                    nums1[count], nums1[i] = nums1[i], nums1[count]
                    i += 1
                else:
                    nums1[count] = nums2.pop(0)
                print(nums1)
            elif i >= len(nums1) and nums2:
                nums1[count] = nums2.pop(0)
            elif i < len(nums1) and not nums2:
                nums1[count], nums1[i] = nums1[i], nums1[count]
                i += 1
            count += 1



class Solution2:
    #从后面开始跑(m+n-1)
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_idx = m - 1
        nums2_idx = n - 1
        index = m + n - 1
        while index >= 0 and nums2_idx >= 0:
            if nums1_idx >= 0 and nums1[nums1_idx] > nums2[nums2_idx]:
                nums1[index] = nums1[nums1_idx]
                nums1[nums1_idx] = 0
                nums1_idx -= 1
            else:
                nums1[index] = nums2[nums2_idx]
                nums2_idx -= 1
            index -= 1

k = Solution()
a = [4, 0, 0, 0, 0, 0]
print(k.merge(a, 1, [1, 2, 3, 5, 6], 5))
print(a)
