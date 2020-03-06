from typing import List
from collections import deque
import heapq


class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        n = len(nums)
        if n * k == 0:
            return []

        return [max(nums[i:i + k]) for i in range(n - k + 1)]





class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        length = len(nums)
        if k >= length: return [max(nums)]
        if k==1:return nums
        result = []
        heap = []
        for i in range(k-1):
            heap.append(-nums[i])

        idx = k - 1

        while idx < length:
            heap.append(-nums[idx])
            heapq.heapify(heap)
            result.append(-heap[0])
            idx += 1
            heap.remove(-nums[idx - k])
            #这个地方不好，因为删除的狮虎为O(n)
        return result


class Solution3:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        #基本思路是分出k大的区间，左右线性扫描最大值
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        left = [0] * n
        left[0] = nums[0]
        right = [0] * n
        right[n - 1] = nums[n - 1]
        for i in range(1, n):
            # from left to right
            if i % k == 0:
                # block start
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])
            # from right to left
            j = n - i - 1
            if (j + 1) % k == 0:
                # block end
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        output = []
        for i in range(n - k + 1):
            output.append(max(left[i + k - 1], right[i]))

        return output


from collections import deque


class Solution4:
    #用一个双向队列保存最大值，队列中保存的是坐标
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        # base cases
        n = len(nums)
        if n * k == 0:
            return []
        if k == 1:
            return nums

        def clean_deque(i):
            # remove indexes of elements not from sliding window
            if deq and deq[0] == i - k:
                deq.popleft()

            # remove from deq indexes of all elements
            # which are smaller than current element nums[i]
            while deq and nums[i] > nums[deq[-1]]:
                deq.pop()

        # init deque and output
        deq = deque()
        max_idx = 0
        for i in range(k):
            clean_deque(i)
            deq.append(i)
            # compute max in nums[:k]
            if nums[i] > nums[max_idx]:
                max_idx = i
        output = [nums[max_idx]]

        # build output
        for i in range(k, n):
            clean_deque(i)
            deq.append(i)
            output.append(nums[deq[0]])
        return output






k=Solution()
print(k.maxSlidingWindow(nums = [1,3,-1,-3,5,3,6,7], k = 3))
