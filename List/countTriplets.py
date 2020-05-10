from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        cumxor = [0]
        n = len(arr)
        ans=0
        for i in range(n):
            cumxor.append(cumxor[i] ^ arr[i])
        for i in range(1, n):
            for j in range(i + 1, n + 1):
                for k in range(j, n + 1):
                    a = cumxor[j - 1] ^ cumxor[i - 1]
                    b = cumxor[k] ^ cumxor[j - 1]
                    if a==b:
                        ans+=1
        return ans

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        if len(arr)<2:
            return 0
        ans=0
        for i in range(len(arr)):
            temp=arr[i]
            for j in range(i+1,len(arr)):
                temp=temp^arr[j]
                if temp==0:
                    ans+=j-i
        return ans



k = Solution()
print(k.countTriplets(arr = [7,11,12,9,5,2,7,17,22]))
