from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from collections import Counter,defaultdict

        def count(answer,current,start,group):
            if current==target:
                answer.append(group.copy())
            elif current<target:
                for i in range(start+1,n):
                    if current+candidates[i]>target:
                        break
                    if i>start+1 and candidates[i]==candidates[i-1]:
                        continue
                    group.append(candidates[i])
                    count(answer,current+candidates[i],i,group)
                    group.pop(-1)


        n=len(candidates)
        candidates.sort()
        answer=[]
        g=[]
        count(answer,0,-1,g)
        return answer

k=Solution()
print(k.combinationSum2([10,1,2,7,6,1,5],8))
