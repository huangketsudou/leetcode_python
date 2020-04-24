from typing import List
import bisect

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:return 0
        tmp = [0] * n
        ans = self.mergesort(nums, tmp, 0, n - 1)
        return ans

    def mergesort(self, nums, tmp, left, right):
        if left == right:
            return 0
        mid = left + (right - left) // 2
        leftPairs = self.mergesort(nums, tmp, left, mid)
        rightPairs = self.mergesort(nums, tmp, mid + 1, right)
        if nums[mid]<nums[mid+1]:return leftPairs+rightPairs
        mergePairs = self.merge(nums, tmp, left, right, mid)

        return leftPairs + rightPairs + mergePairs

    def merge(self, nums, tmp, left, right, mid):
        i, j = left, mid + 1
        ans = 0
        for k in range(left, right + 1):
            if i > mid:
                tmp[k] = nums[j]
                j += 1
            elif j > right:
                tmp[k] = nums[i]
                i += 1
            elif nums[i] <= nums[j]:
                tmp[k] = nums[i]
                i += 1
            else:
                tmp[k] = nums[j]
                j += 1
                ans += (mid + 1 - i)
            k += 1
        nums[left:right + 1] = tmp[left:right + 1]
        return ans


class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    @staticmethod
    def lowbit(x):
        #只保留最后一个数为的1
        return x & (-x)

    def query(self, x):
        ret = 0
        while x > 0:
            ret += self.tree[x]
            x -= BIT.lowbit(x)
        return ret

    def update(self, x):
        while x <= self.n:
            self.tree[x] += 1
            x += BIT.lowbit(x)#这里看不懂，大概猜想是利用最低为做划分，每次进1位，这个范围内的数都要加1


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        # 离散化
        tmp = sorted(nums)
        for i in range(n):
            nums[i] = bisect.bisect_left(tmp, nums[i]) + 1
        # 树状数组统计逆序对
        '''
        离散化的思想是，只关心数字之间的相对大小，而不关心绝对大小
        对于数组[1,2,3,5,4,6,4,2,3]
        排序后[1, 2, 2, 3, 3, 4, 4, 5, 6]
        离散化之后[1, 2, 4, 8, 6, 9, 6, 2, 4]，就是原数字在排序之后的最小排名
        '''
        bit = BIT(n)
        ans = 0
        for i in range(n - 1, -1, -1):
            ans += bit.query(nums[i] - 1)
            bit.update(nums[i])
            print(bit.tree)
        return ans


