from typing import List


class Solution:
    # 确定某一根火柴要放在那个正方形边的组中
    def makesquare(self, nums: List[int]) -> bool:
        if not nums: return False
        n = len(nums)
        permiter = sum(nums)
        possible_side = permiter // 4
        if possible_side * 4 != permiter:
            return False
        nums.sort(reverse=True)
        sums = [0 for _ in range(4)]

        def dfs(idx):
            if idx == n:
                return sums[0] == sums[1] == sums[2] == possible_side
            for i in range(4):
                if sums[i] + nums[idx] <= possible_side:
                    sums[i] += nums[idx]
                    if dfs(idx + 1):
                        return True
                    sums[i] -= nums[idx]
            return False

        return dfs(0)


class Solution:
    # 状态压缩，mask掩码，1表示这根火柴还没有被用过，可以使用
    def makesquare(self, nums: List[int]) -> bool:
        if not nums: return False
        n = len(nums)
        perimeter = sum(nums)
        possible_side = perimeter // 4
        if possible_side * 4 == perimeter: return False
        memo = {}
        def dfs(mask, sides_done):
            total = 0
            for i in range(n - 1, -1, -1):#这里的for循环作用是计算所有已经被用掉的火柴边的总长度
                if not (mask & (1 << i)):
                    total += nums[n - 1 - i]
            if total > 0 and total % possible_side == 0:
                sides_done += 1
            if sides_done == 3:
                return True
            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]
            ans = False
            c = int(total / possible_side)
            rem = possible_side * (c + 1) - total#计算当前要构成下一完整的边需要多长的火柴
            for i in range(n - 1, -1, -1):
                if nums[n - 1 - i] <= rem and mask & (1 << i):
                    if dfs(mask ^ (1 << i), sides_done):
                        ans = True
                        break
            memo[(mask, sides_done)] = ans
            return ans

        return dfs((1 << n) - 1, 0)
