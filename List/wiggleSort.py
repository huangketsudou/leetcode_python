from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2: return
        mid = (0 + n - 1) // 2  # 中位数索引

        # 快速排序中的一次划分
        # 这里需要把数组分成两组，左边的数比中位数小，右边的数比中位数大，当数据中存在重复数值时，
        def partition(begin, end):
            left, right = begin, end
            while left < right:
                while left < right and nums[left] < nums[right]: right -= 1
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                while left < right and nums[left] < nums[right]: left += 1
                if left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1
            return left

        # 找到中位数对应的数值
        left, right = 0, n - 1
        while True:
            pivot = partition(left, right)
            if pivot == mid:
                break
            elif pivot > mid:
                right = pivot - 1
            else:
                left = pivot + 1

        # 三路划分(荷兰旗)
        # 把中位数集中到中间，然后倒序开始排序
        midNum = nums[mid]
        left, curr, right = 0, 0, n - 1
        while curr < right:
            if nums[curr] < midNum:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
                curr += 1
            elif nums[curr] > midNum:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1

        # 交叉合并，空间O(N)
        # small, big, _nums = mid, n - 1, nums[:]
        # for i in range(n):
        #     if i % 2 == 0:
        #         nums[i] = _nums[small]
        #         small -= 1
        #     else:  # big
        #         nums[i] = _nums[big]
        #         big -= 1
        # 空间O(1)
        A = lambda i: (1 + 2 * (i)) % (n | 1)
        i, j, k = 0, 0, n - 1

        while j <= k:
            print(nums)
            print(i,j,k)
            if nums[A(j)] > midNum:
                nums[A(i)], nums[A(j)] = nums[A(j)], nums[A(i)]
                i += 1
                j += 1
            elif nums[A(j)] < midNum:
                nums[A(j)], nums[A(k)] = nums[A(k)], nums[A(j)]
                k -= 1
            else:
                j += 1


class Solution2:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        mid = len(nums) // 2
        nums[1::2], nums[0::2] = nums[:mid], nums[mid:]


k = Solution()
print(k.wiggleSort([5, 3, 1, 2, 6, 7, 8, 5, 5]))
