from typing import List
import math


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        if n < 3: return 0
        left = 0
        right = 1
        sub = A[right] - A[left]
        ans = 0
        while right < n:
            if right == n - 1 or A[right + 1] - A[right] != sub:
                k = right - left + 1
                if k >= 3:
                    ans += (k-2)*(k-1)//2
                left=right
                right=right+1

                #     left = right + 1
                #     right += 2
                # else:
                #     left+=1
                #     right+=1
                if right < n:
                    sub = A[right] - A[left]
            else:
                right += 1
        return ans


k=Solution()
print(k.numberOfArithmeticSlices([1,2,3,4,6,8]))