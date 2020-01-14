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



class Solution2:
    #k个数的组合和，不允许重复
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        answer = []
        tmp = []

        def core(temp,end):

            for i in range(end,10):
                if len(temp)+1==k:
                    if sum(temp)+i==n:
                        answer.append(temp+[i])
                    elif sum(temp)+i>n:
                        break
                    else:
                        continue
                else:
                    if sum(temp)+i>=n:
                        break
                    else:
                        core(temp+[i],i+1)


        core(tmp,1)
        return answer
