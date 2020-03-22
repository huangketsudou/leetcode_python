class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        n=len(nums)
        if n==0:return []
        target=[]
        for i in range(n):
            idx=index[i]
            number=nums[i]
            target.insert(idx,number)
        return target
