class MountainArray:
    def get(self, index: int) -> int:
        pass

    def length(self) -> int:
        pass


class Solution:

    # 把他分解为两个单调子区间,在两个子区间进行判断
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()
        left, right = 0, n - 1
        while left < right:  # 从山峰数组中找到顶峰
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid
        peak = left
        index = self.binarysearch(mountain_arr, target, 0, peak)
        if index != -1:
            return index
        index = self.binarysearch(mountain_arr, target, peak + 1, mountain_arr.length() - 1, lambda x: -x)
        #把递减的数组转为递增的数组
        return index

    def binarysearch(self, mountain, target, l, r, key=lambda x: x):
        target = key(target)
        while l <= r:#因为这里允许数字不存在，所以用<=,如果用<,那么最后还要判断num[left]==target
            mid = (l + r) // 2
            cur = key(mountain.get(mid))
            if cur == target:
                return mid
            elif cur < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1
