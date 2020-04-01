class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        diamond=set(J)
        ans=0
        for s in S:
            if s in diamond:
                ans+=1
        return ans
