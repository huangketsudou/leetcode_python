from typing import List
from collections import deque


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:return []
        result=[]
        stack=deque()
        stack.append(nums[0])
        for i in nums[1:]:
            if i-stack[-1]!=1:
                if len(stack)==1:
                    result.append(str(stack.pop()))
                else:
                    result.append('{}->{}'.format(stack.popleft(),stack.pop()))
                    stack.clear()
            stack.append(i)

        if len(stack)!=0:
            if len(stack) == 1:
                result.append(str(stack.pop()))
            else:
                result.append('{}->{}'.format(stack.popleft(), stack.pop()))
                stack.clear()
        return result


class Solution2:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        # 一直动的指针
        i = 0
        n = len(nums)
        res = []
        while i < n:
            # 记录开始的指针
            start = i
            while i < n - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            # 相等说明, 只有一个数
            if start == i:
                res.append(str(nums[i]))
            else:
                res.append("{}->{}".format(nums[start], nums[i]))
            i += 1
        return res



k=Solution()
print(k.summaryRanges([0,2,3,4,6,8,9]))
