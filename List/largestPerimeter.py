class Solution(object):
    def largestPerimeter(self, A):
        A.sort()
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0

class Solution2(object):
    def largestPerimeter(self, A):
        A.sort(reverse=True)
        for i in range(2,len(A)):
            if A[i-2]<A[i-1]+A[i]:
                return A[i]+A[i-2]+A[i-1]
        return 0
