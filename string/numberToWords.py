from typing import List
from collections import deque
import heapq
from heapq import heappush, heappop
import functools


class Solution:
    def numberToWords(self, num: int) -> str:

        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def core(number):
            if number < 20:
                return to19[number - 1:number]
            if number < 100:
                return [tens[number // 10 - 2]] + core(number % 10)
            if number < 1000:
                return [to19[number // 100 - 1]] + ["Hundred"] + core(number % 100)

        result = []
        for key, v in {1000000000: 'Billion', 1000000: 'Million', 1000: 'Thousand', 1: ''}.items():
            if num >= key:
                result += core(num // key) + [v]
                num %= key

        return ' '.join(result).strip() or 'zero'


k = Solution()
print(k.numberToWords(1234567))


class Solution2:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
               'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

        def helper(num):
            if num < 20:
                return to19[num - 1:num]
            if num < 100:
                return [tens[num // 10 - 2]] + helper(num % 10)
            if num < 1000:
                return [to19[num // 100 - 1]] + ["Hundred"] + helper(num % 100)
            for p, w in enumerate(["Thousand", "Million", "Billion"], 1):
                if num < 1000 ** (p + 1):
                    return helper(num // 1000 ** p) + [w] + helper(num % 1000 ** p)

        return " ".join(helper(num)) or "Zero"


g = Solution2()
print(g.numberToWords(12000001))
