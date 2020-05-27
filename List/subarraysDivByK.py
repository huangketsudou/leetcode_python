from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        n = len(A)
        if not n:
            return 0
        dictionary = defaultdict(int)
        dictionary[0] = 1
        prev = 0
        ans = 0
        for i in range(n):
            cur = prev + A[i]
            ans += dictionary[cur % K]
            ans += dictionary[K - cur % K]
            dictionary[cur % K] += 1
            prev = cur
        return ans

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        record = {0: 1}
        total = 0
        for elem in A:
            total += elem
            modulus = total % K
            record[modulus] = record.get(modulus, 0) + 1

        ans = 0
        for x, cx in record.items():
            ans += cx * (cx - 1) // 2
        return ans

