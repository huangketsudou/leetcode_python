#仅有一个数字出现了1次，其他两次
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result=0
        for i in nums:
            result^=i
        return result

class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)

class Solution3(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]




k=Solution()
print(k.singleNumber([2,2,4,4,3]))

#-------------------------------
#列表中仅有一个数字只出现了一次，其他出现了3次
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones, twos = 0, 0
        for i in nums:
            ones = ones ^ i & ~ twos
            twos = twos ^ i & ~ ones
        return ones
