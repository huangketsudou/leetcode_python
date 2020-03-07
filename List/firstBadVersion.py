class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=1
        right=n
        while left<right:
            middle=(left+right)//2
            if isBadVersion(middle):
                right=middle
            else:
                left=middle+1
        return left
    
