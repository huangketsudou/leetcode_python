from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:

        number = [0] * 201
        for i in A:
            number[i + 100] += 1
        i = 0
        while K > 0:
            while number[i] == 0:
                i += 1
            number[i] -= 1
            number[200 - i] += 1
            if i > 100:
                i = 200 - i
            K -= 1
        sum=0
        for j in range(i,len(number)):
            sum+=(j-100)*number[j]
        return sum
