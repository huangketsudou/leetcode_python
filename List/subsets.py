from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #利用了combine的函数内容
        def combinations(iterable, r):
            # combinations('ABCD', 2) --> AB AC AD BC BD CD
            # combinations(range(4), 3) --> 012 013 023 123
            pool = tuple(iterable)
            n = len(pool)
            if r > n:
                return
            indices = list(range(r))
            yield tuple(pool[i] for i in indices)  # 对应solution3最开始加入的一个情况
            # 这个算法主要比较像把所要求的指标逐个后移
            while True:
                for i in reversed(range(r)):
                    if indices[i] != i + n - r:
                        break
                else:
                    return
                indices[i] += 1
                for j in range(i + 1, r):
                    indices[j] = indices[j - 1] + 1
                yield tuple(pool[i] for i in indices)
        n=len(nums)
        answer=[]
        for i in range(0,n+1):
            for j in combinations(nums,i):
                answer.append(list(j))
        return answer


k=Solution()
print(k.subsets([1,2,3]))
