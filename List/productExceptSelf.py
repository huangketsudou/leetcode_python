from typing import List
from collections import deque


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftproduct=[1]
        rightproduct=[1]


        for i in nums:
            leftproduct.append(leftproduct[-1]*i)
        leftproduct.append(1)
        for i in nums[::-1]:
            rightproduct.append(rightproduct[-1]*i)
        rightproduct.append(1)
        rightproduct.reverse()
        result=[]
        for j in range(1,len(leftproduct)-1):
            result.append(leftproduct[j-1]*rightproduct[j+1])
        return result



class Solution2:
    def from typing import List
from collections import deque


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        leftproduct=[1]
        rightproduct=[1]


        for i in nums:
            leftproduct.append(leftproduct[-1]*i)
        leftproduct.append(1)
        for i in nums[::-1]:
            rightproduct.append(rightproduct[-1]*i)
        rightproduct.append(1)
        rightproduct.reverse()
        result=[]
        for j in range(1,len(leftproduct)-1):
            result.append(leftproduct[j-1]*rightproduct[j+1])
        return result



class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length=len(nums)
        result=[0]*length
        result[0]=1
        for i in range(1,length):
            result[i]=nums[i-1]*result[i-1]
        R=1
        for j in range(length-1,-1,-1):
            result[j]=R*result[j]
            R*=nums[j]

        return result







k=Solution()
print(k.productExceptSelf([1,2,3,4]))(self, nums: List[int]) -> List[int]:
        length=len(nums)
        result=[0]*length
        result[0]=1
        for i in range(1,length):
            result[i]=nums[i-1]*result[i-1]
        R=1
        for j in range(length-1,-1,-1):
            result[j]=R*result[j]
            R*=nums[j]

        return result







k=Solution()
print(k.productExceptSelf([1,2,3,4]))
