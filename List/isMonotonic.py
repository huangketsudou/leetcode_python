class Solution(object):
    def isMonotonic(self, A):
        return all(A[i]<=A[i+1] for i in range(len(A)-1)) or \
        all(A[j]>=A[j+1] for j in range(len(A)-1))


class Solution(object):
    def isMonotonic(self, A):
        store = 0
        for i in range(len(A) - 1):
            c = cmp(A[i], A[i+1])#python3已经移除了
            if c:
                if c != store != 0:
                    return False
                store = c
        return True
