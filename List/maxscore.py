from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if n == k:
            return sum(cardPoints)
        left = [0] * (n + 1)
        right = [0] * (n + 1)
        for i in range(1,n+1):
            left[i]=left[i-1]+cardPoints[i-1]
        for j in range(n-1,-1,-1):
            right[j]=right[j+1]+cardPoints[j]
        ans=0
        for p in range(k+1):
            ans=max(ans,left[p]+right[n-k-p])
        return ans


class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        s=sum(cardPoints[:k])
        t=s
        for i in range(k):
            t+=cardPoints[-i-1]-cardPoints[k-i-1]
            s=max(s,t)
        return s