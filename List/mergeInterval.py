from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n=len(intervals)
        if n==0:return []
        ans=[]
        curleft,curright=intervals[0]
        i=1
        while i<n:
            nxleft,nxright=intervals[i]
            if curright>=nxleft:
                curright=max(nxright,curright)
            else:
                ans.append([curleft,curright])
                curleft,curright=nxleft,nxright
            i+=1
        ans.append([curleft,curright])
        return ans

k=Solution()
print(k.merge([[1,4],[4,5]]))