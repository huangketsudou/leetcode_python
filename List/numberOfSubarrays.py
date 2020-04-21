from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = [-1]
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 1:
                odd.append(i)
        rightborder = n
        m = len(odd)
        if m < k: return 0
        ans = 0
        right = left = m - 1
        while left > 0:
            if right-left+1 < k:
                left -= 1
            elif left > 0:
                ans += (odd[left] - odd[left - 1]) * (rightborder - odd[right])
                rightborder = odd[right]
                right -= 1
        return ans


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        odd = [-1]
        ans = 0
        for i in range(n):
            if nums[i] % 2 == 1:
                odd.append(i)
        odd.append(n)
        print(odd)
        for i in range(1, len(odd) - k):
            ans += (odd[i] - odd[i - 1]) * (odd[i + k] - odd[i + k - 1])
        return ans



class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        cnt = [0] * (len(nums) + 1)
        cnt[0] = 1
        odd, ans = 0, 0
        for num in nums:
            if num%2==1:
                odd+=1
            if odd>=k:
                ans+=cnt[odd-k]
            cnt[odd]+=1
        return ans


k = Solution()
print(k.numberOfSubarrays(nums = [1,1,2,1,2,1,1], k = 5))
