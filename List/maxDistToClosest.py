class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        ans = [float('inf')] * n
        prev = -1
        for i, v in enumerate(seats):
            if prev == -1 and v != 1:
                continue
            elif v==1:
                prev = i
            ans[i] = i - prev
        prev = -1
        for i in range(n - 1, -1, -1):
            if prev == -1 and seats[i] != 1:
                continue
            elif seats[i]==1:
                prev = i
            ans[i] = min(ans[i], prev - i)
        return max(ans)


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        rightnxt=(i for i,seat in seats if seat)
        prev,nxt=None,next(rightnxt)

        ans=0
        for i,seat in enumerate(seats):
            if seat:
                prev=i
            else:
                while nxt is not None and nxt<i:
                    nxt=next(rightnxt,None)
                left=float('inf') if prev is None else i-prev
                right=float('inf') if nxt is None else nxt-i
                ans=max(ans,min(left,right))
        return ans
    


k = Solution()
b=[1,0,0,0,1,0,1]
c=[1,0,0,0]
print(k.maxDistToClosest(c))
