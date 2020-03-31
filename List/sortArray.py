class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n < 2: return nums
        left = []
        right = []
        pivot = nums[0]
        for i in range(1, n):
            if nums[i] <= pivot:
                left.append(nums[i])
            else:
                right.append(nums[i])
        return self.sortArray(left) + [pivot] + self.sortArray(right)


class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.inplace_sort(nums, 0, len(nums) - 1)
        return nums

    def inplace_sort(self, S, a, b):
        if a > b: return
        pivot = S[b]
        left, right = a, b - 1
        while left <= right:
            while left <= right and S[left] < pivot:
                left += 1
            while right >= left and S[right] > pivot:
                right -= 1
            if left <= right:
                S[left], S[right] = S[right], S[left]
                left, right = left + 1, right - 1
        S[left], S[b] = S[b], S[left]
        self.inplace_sort(S, a, left - 1)
        self.inplace_sort(S, left + 1, b)


class Solution3:
    def sortArray(self, nums: List[int]) -> List[int]:

        self.mergesort(nums)
        return nums

    def mergesort(self, nums):
        n = len(nums)
        if n < 2: return
        nums1 = nums[:n // 2]
        nums2 = nums[n // 2:]
        self.sortArray(nums1)
        self.sortArray(nums2)
        self.merge(nums1, nums2, nums)

    def merge(self, S1, S2, S):
        i = j = 0
        while i + j < len(S):
            if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
                S[i + j] = S1[i]
                i += 1
            else:
                S[i + j] = S2[j]
                j += 1

    def mergebehind(self, S1, S2, S):
        i, j, idx = len(S1) - 1, len(S2) - 1, len(S) - 1
        while idx >= 0:
            if i < 0:
                p = S2[j]
                j -= 1
            elif j < 0:
                p = S1[i]
                i -= 1
            else:
                if S1[i] <= S2[j]:
                    p = S2[j]
                    j -= 1
                else:
                    p = S1[i]
                    i -= 1
            S[idx] = p
            idx -= 1


k = Solution()
print(k.sortArray([1, 23, -1, 4, 5, 76, 0, 2, 3, 0, 0, 1, 2, 3, 4, 984, 39, 23, 5, 211, 314]))
