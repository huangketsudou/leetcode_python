from typing import List


class Solution:
    #图：法官点定义为入读为N-1而出度为0的点
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        indegree=[0]*(N+1)
        outdegree=[0]*(N+1)
        for outd,ind in trust:
            indegree[ind]+=1
            outdegree[outd]+=1

        for i in range(1,N+1):
            if indegree[i]==N-1 and outdegree[i]==0:
                return i
        return -1


