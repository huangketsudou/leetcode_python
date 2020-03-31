class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost+=[0]
        n=len(cost)
        leastcost=[0]*n
        leastcost[0]=cost[0]
        leastcost[1]=min(cost[0]+cost[1],cost[1])
        for i in range(2,n):
            leastcost[i]=min(leastcost[i-1],leastcost[i-2])+cost[i]
        return leastcost[-1]

class Solution2(object):
    def minCostClimbingStairs(self, cost):
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)




k=Solution()
print(k.minCostClimbingStairs([10,15,20]))
