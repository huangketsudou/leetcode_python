from typing import List


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n==1:return '1'
        k -= 1
        w = [i for i in range(1, n + 1)]
        tmp = [1]
        for i in range(2, n):
            tmp.append(tmp[-1] * i)
        tmp = reversed(tmp)
        answer=''
        for i in tmp:
            index = k // i
            k %= i
            answer+=str(w.pop(index))
        answer+=str(w.pop())
        return answer


k = Solution()
print(k.getPermutation(3, 6))
