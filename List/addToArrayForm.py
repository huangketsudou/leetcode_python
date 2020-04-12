from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        carry = 0
        idx = len(A) - 1
        while (carry or K) and idx >= 0:
            digit, K = K % 10, K // 10
            summary = A[idx] + carry + digit
            A[idx], carry = summary % 10, summary // 10
            idx -= 1
        if K + carry != 0:
            A=list(map(int,str(K+carry)))+A
        return A

