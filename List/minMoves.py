class Solution:
    def minMoves(self, nums: List[int]) -> int:

        nums.sort()
        moves=0
        for i in range(1,len(nums)):
            moves+=nums[i]-nums[0]
        return moves

class Solution2:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        moves=0
        for i in range(1,len(nums)):
            diff=nums[i]+moves-nums[i-1]
            nums[i]+=moves
            moves +=diff
        print(nums)
        return moves

k=Solution2()
print(k.minMoves([1,2,3,4]))
