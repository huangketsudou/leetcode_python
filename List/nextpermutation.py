class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if n-1<=0:
            return
        j=n-1
        while j>0:
            if nums[j-1]<nums[j]:
                break
            j-=1
        if j==0:
            nums.reverse()
            return
        k=j
        while k<n:
            if nums[k]<=nums[j-1]:
                break
            k+=1
        k-=1
        nums[j-1],nums[k]=nums[k],nums[j-1]
        nums[j:]=reversed(nums[j:])
