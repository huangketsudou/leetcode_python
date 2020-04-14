from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod = [0] * 60
        for song in time:
            mod[song % 60] += 1
        ans = mod[0] * (mod[0] - 1) // 2 + mod[30] * (mod[30] - 1) // 2
        left, right = 1, 59
        while left < right:
            ans += mod[left] * mod[right]
            left += 1
            right -= 1
        return ans


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod = [0] * 60
        ans = 0
        for song in time:
            left = song % 60
            if left!=0:
                ans+=mod[60-left]
            else:
                ans+=mod[left]
            mod[left]+=1
        return ans