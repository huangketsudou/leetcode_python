from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.size = len(nums)
        self.cunsum = [0] * (self.size + 1)
        for i in range(1, self.size + 1):
            self.cunsum[i] = self.cunsum[i - 1] + self.array[i - 1]

    def update(self, i: int, val: int) -> None:
        sub = val - self.array[i]
        self.array[i] = val
        for i in range(i, self.size + 1):
            self.cunsum[i] += sub

    def sumRange(self, i: int, j: int) -> int:
        return self.cunsum[j + 1] - self.cunsum[i]


class NumArray:

    def __init__(self, nums: List[int]):
        self.size = len(nums)
        self.tree = [0] * 2 * self.size
        self.buildtree(nums)

    def buildtree(self, nums):
        j = 0
        for i in range(self.size, 2 * self.size):
            self.tree[i] = nums[j]
            j += 1
        for i in range(self.size - 1, -1, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[2 * i + 1]

    def update(self, i: int, val: int) -> None:
        i += self.size
        self.tree[i] = val
        while i > 0:
            left = i
            right = i
            if i % 2 == 0:
                right = i + 1
            else:
                left = i - 1
            self.tree[i // 2] = self.tree[left] + self.tree[right]
            i //= 2

    def sumRange(self, i: int, j: int) -> int:
        i+=self.size
        j+=self.size
        sum=0
        while i<=j:
            if i%2==1:
                sum+=self.tree[i]
                i+=1 #通过这个来切换左右子树
                #i是左子树，如果其是偶数，则在下一层再加，否则加上
            if j%2==0:
                sum+=self.tree[j]
                j-=1 #通过这个来切换左右子树
                #j是右子树，如果其是奇数，则在下一层再加，否则加上
            i//=2
            j//=2
        return sum
