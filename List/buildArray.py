from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        k = 0
        ans = []
        m = len(target)
        for i in range(1, n + 1):
            ans.append('Push')
            if i != target[k]:
                ans.append('Pop')
            else:
                k += 1
                if k == m: break
        return ans
