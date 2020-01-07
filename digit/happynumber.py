from typing import List
import functools
import math
import itertools


class Solution:
    def isHappy(self, n: int) -> bool:
        seen=set()
        seen.add(1)
        while n!=1:
            n=sum([int(i)**2 for i in str(n)])
            if n in seen:
                return n==1
            seen.add(n)

class Solution2:
    #解决循环问题的一种有效方法时快慢指针
    #对于快乐数，他的循环体只有一个数1，而非快乐数，循环体中一定没有1
    def isHappy(self, n: int) -> bool:
        n = str(n)
        slow = n
        fast = str(sum(int(i) ** 2 for i in n))
        while slow != fast:
            slow = str(sum(int(i) ** 2 for i in slow))
            fast = str(sum(int(i) ** 2 for i in fast))
            fast = str(sum(int(i) ** 2 for i in fast))
        return slow == "1"



k=Solution()
print(k.isHappy(19))
