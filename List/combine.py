from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer=[]
        tmp=[]
        self.core(n,k,0,answer,tmp)
        return answer


    def core(self,n,k,start,answer,tmp):
        if len(tmp)==k:
            answer.append(tmp.copy())
        else:
            for i in range(start+1,n+1):
                tmp.append(i)
                self.core(n,k,i,answer,tmp)
                tmp.pop(-1)


class Solution2:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combinations(iterable, r):
            # combinations('ABCD', 2) --> AB AC AD BC BD CD
            # combinations(range(4), 3) --> 012 013 023 123
            pool = tuple(iterable)
            n = len(pool)
            if r > n:
                return
            indices = list(range(r))
            yield tuple(pool[i] for i in indices)#对应solution3最开始加入的一个情况
            #这个算法主要比较像把所要求的指标逐个后移
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

        answer=[]
        for i in combinations(list(range(1,n+1)),k):
            answer.append(list(i))

        return answer


class Solution3:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # init first combination
        nums = list(range(1, k + 1)) + [n + 1]
        print(nums)
        output, j = [], 0
        while j < k:
            # add current combination
            print(nums[:k])
            output.append(nums[:k])
            # increase first nums[j] by one
            # if nums[j] + 1 != nums[j + 1]
            j = 0
            while j < k and nums[j + 1] == nums[j] + 1:
                nums[j] = j + 1
                j += 1
            nums[j] += 1

        return output



k=Solution3()
print(k.combine(5,3))
