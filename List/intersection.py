from typing import List
from collections import deque
import heapq
from heapq import heappush, heappop
import functools
import math
from collections import deque


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        for num in nums1:
            if num in result:
                continue
            if num in nums2:
                result.append(num)

        return result


class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)



class Solution:
    def set_intersection(self, set1, set2):
        num1=set(set1)
        num2=set(set2)

        return list(num1 & num2)
