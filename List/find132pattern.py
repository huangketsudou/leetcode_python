from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        le = len(nums)
        if le < 2: return False

        mi = [nums[0]]
        for i in range(1, le):
            mi.append(min(nums[i], mi[-1]))

        stack = []
        for i in range(le - 1, -1, -1):
            print(stack)
            if nums[i] > mi[i]:
                while stack and mi[i] >= stack[-1]:
                    stack.pop()

                if stack and stack[-1] < nums[i]:
                    return True
                stack.append(nums[i])
        return False


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        ak = float("-inf")
        stack = []
        for num in reversed(nums):
            if ak > num: return True
            while stack and stack[-1] < num:
                ak = stack.pop()
            stack.append(num)
        return False
