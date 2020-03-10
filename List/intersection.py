from typing import List
from collections import deque
import heapq
from heapq import heappush, heappop
import functools
import math
from collections import deque

#不考虑重复元素
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

    
    
#--------------------------------------------------------------------
#考虑重复元素，交集包括重复元素
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n2=Counter(nums2)
        result=[]
        for num in nums1:
            if num in n2 and n2[num]!=0:
                result.append(num)
                n2[num]-=1
        return result

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        p1=p2=0
        result=[]
        while p1<len(nums1) and p2<len(nums2):
            if nums1[p1]==nums2[p2]:
                result.append(nums1[p1])
                p1+=1
                p2+=1
            elif nums1[p1]<nums2[p2]:
                p1+=1
            else:
                p2+=1
        return result




k=Solution()
print(k.intersect(nums1 = [1,2,2,1], nums2 = [2,2]))
