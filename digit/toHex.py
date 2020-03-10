from typing import List
from collections import deque
import heapq
from heapq import heappush, heappop
import functools
import math
from collections import deque
from collections import Counter
from itertools import combinations, product


class Solution:
    def toHex(self, num: int) -> str:
        digit = "0123456789abcdef"
        a = num & 0xffffffff
        result = ''
        while a:
            div, mod = divmod(a, 16)
            result = digit[mod] + result
            a = div
        return result


class Solution:
    def toHex(self, num: int) -> str:
        num &= 0xFFFFFFFF
        s = "0123456789abcdef"
        res = ""
        mask = 0b1111
        while num > 0:
            res += s[num & mask]
            num >>= 4
        return res[::-1] if res else "0"


k = Solution()
print(k.toHex(26))
