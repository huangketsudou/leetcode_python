class Solution:
    def checkPossibility(self, nums: list) -> bool:
        length = len(nums)
        count = 0  # 这个计数器用于统计下降点的个数
        for i in range(length-1):
            if nums[i]>nums[i+1]:
                # 判断出现的一个下降点能否只动一个数就变成符合条件的数列
                if i-1>=0 and nums[i-1]>nums[i+1] and i+2<=length-1 and nums[i+2]<nums[i]:
                    return False
                count += 1
                # 如果下降点多于1个，自然返回False
                if count >1:
                    return False
        return True

