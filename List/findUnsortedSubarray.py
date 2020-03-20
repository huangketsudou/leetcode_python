class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        tmp = nums.copy()
        tmp.sort()
        i = 0
        n = len(nums)
        while nums[i] == tmp[i]:
            i += 1

        j = n - 1
        while nums[j] == tmp[j]:
            j -= 1

        return j - i + 1


class Solution2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        n = len(nums)
        l = n
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                l = min(stack.pop(), l)
            stack.append(i)
        g = 0
        stack = []
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[j]:
                g = max(g, stack.pop())
            stack.append(j)
        return g - l + 1 if g > l else 0


class Solution3:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        s = float('inf')
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                s = min(nums[i], s)
        sid = n

        for i in range(n):
            if nums[i] > s:
                sid = i
                break
        g = float('-inf')

        for j in range(n - 2, -1, -1):
            if nums[j] > nums[j + 1]:
                g = max(g, nums[j])

        gid = 0
        for j in range(n - 1, -1, -1):
            if nums[j]<g:
                gid=j
                break

        return gid-sid+1 if sid<gid else 0

k = Solution3()
print(k.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
