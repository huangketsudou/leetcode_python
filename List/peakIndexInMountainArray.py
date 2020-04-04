class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(1,len(A)):
            if A[i]<A[i-1]:
                return i-1


class Solution2:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        left,right=0,len(A)-1
        while left<right:
            mid=left+(right-left)//2
            if A[mid]<A[mid+1]:
                left=mid+1
            else:
                right=mid
        return left

k=Solution()
print(k.peakIndexInMountainArray([0,2,1,0]))
