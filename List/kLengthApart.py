from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        strnum = ''.join(map(str, nums))
        strnum.strip('0')
        number = int(strnum, base=2)
        number>>=1
        count = 0
        ans = float('inf')
        while number:
            if number & 1:
                ans = min(ans, count)
                count = 0
            count += 1
            number >>= 1
        return ans >= k


k = Solution()
print(k.kLengthApart(nums = [1,0,0], k = 1))
