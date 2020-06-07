class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        length=len(nums)//2
        ans = []
        for i in range(length):
            ans.append(nums[i])
            ans.append(nums[i+length])
        return ans
