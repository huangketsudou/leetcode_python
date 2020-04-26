from typing import List


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # The container that holds all intermediate solutions.
        # key: the largest element in a valid subset.
        subsets = {-1: set()}

        for num in sorted(nums):
            subsets[num] = max([subsets[k] for k in subsets if num % k == 0], key=len) | {num}

        return list(max(subsets.values(), key=len))


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []

        # important step !
        nums.sort()

        # The container that keep the size of the largest divisible subset that ends with X_i
        # dp[i] corresponds to len(EDS(X_i))
        dp = [0] * (len(nums))

        """ Build the dynamic programming matrix/vector """
        for i, num in enumerate(nums):
            maxSubsetSize = 0
            for k in range(0, i):
                if nums[i] % nums[k] == 0:
                    maxSubsetSize = max(maxSubsetSize, dp[k])

            maxSubsetSize += 1
            dp[i] = maxSubsetSize

        """ Find both the size of largest divisible set and its index """
        maxSize, maxSizeIndex = max([(v, i) for i, v in enumerate(dp)])
        ret = []

        """ Reconstruct the largest divisible subset """
        # currSize: the size of the current subset
        # currTail: the last element in the current subset
        currSize, currTail = maxSize, nums[maxSizeIndex]
        for i in range(maxSizeIndex, -1, -1):
            if currSize == dp[i] and currTail % nums[i] == 0:
                ret.append(nums[i])
                currSize -= 1
                currTail = nums[i]

        return reversed(ret)


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        def EDS(i):
            """ recursion with memoization """
            if i in memo:
                return memo[i]

            tail = nums[i]
            maxSubset = []
            # The value of EDS(i) depends on it previous elements
            for p in range(0, i):
                if tail % nums[p] == 0:
                    subset = EDS(p)
                    if len(maxSubset) < len(subset):
                        maxSubset = subset

            # extend the found max subset with the current tail.
            maxSubset = maxSubset.copy()
            maxSubset.append(tail)

            # memorize the intermediate solutions for reuse.
            memo[i] = maxSubset
            return maxSubset

        # test case with empty set
        if len(nums) == 0: return []

        nums.sort()
        memo = {}

        # Find the largest divisible subset
        return max([EDS(i) for i in range(len(nums))], key=len)


