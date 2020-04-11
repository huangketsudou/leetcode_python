class Solution(object):
    def repeatedNTimes(self, A):
        for k in range(1, 4):
            for i in range(len(A) - k):
                if A[i] == A[i+k]:
                    return A[i]



class Solution(object):
    def repeatedNTimes(self, A):
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k

class Solution3(object):
    def repeatedNTimes(self, A):
        i,j,k=0,1,2
        while k<len(A):
            if A[i]==A[j] or A[i]==A[k]:
                return A[i]
            i,j,k=i+1,j+1,k+1
        return A[k-1]

k=Solution3()
print(k.repeatedNTimes([1,2,3,3]))
