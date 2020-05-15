from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 0: return False
        Next = lambda x: (x + nums[x]) % n
        for i in range(n):
            if nums[i] == 0: continue
            fast = slow = i
            slow = Next(slow)
            fast = Next(Next(fast))
            while fast != slow:
                slow = Next(slow)
                fast = Next(Next(fast))
            if slow == Next(slow):
                nums[slow] = 0
                continue
            nxt = Next(slow)
            while fast != nxt:
                if (nums[slow] < 0) != (nums[nxt] < 0):
                    break
                slow = nxt
                nxt = Next(slow)
            else:
                return True
            while nums[fast] != 0:
                nxt = Next(fast)
                nums[fast] = 0
                fast = nxt
        return False


