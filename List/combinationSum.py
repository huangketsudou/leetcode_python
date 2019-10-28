from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def count(current, answer , group,start,size):
            if current == target:
                answer.append(group.copy())
            elif current<target:
                for i in range(start,size):
                    if current+candidates[i]>target:
                        break
                    group.append(candidates[i])
                    count(current+candidates[i],answer,group,i,size)
                    group.pop(-1)

        answer=[]
        candidates.sort()
        n=len(candidates)
        current=0
        g=[]
        count(current,answer,g,0,n)
        return answer





k=Solution()
b=k.combinationSum([2,3,5],8)
print(b)
