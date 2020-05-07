from collections import defaultdict


class Solution:
    '''
    滑动窗口解法，
    https://leetcode-cn.com/problems/longest-repeating-character-replacement/solution/tong-guo-ci-ti-liao-jie-yi-xia-shi-yao-shi-hua-don/
    '''
    def characterReplacement(self, s: str, k: int) -> int:
        if s == '': return 0
        word_num = defaultdict(int)
        left = 0
        n = len(s)
        charmax = 0
        for right in range(n):
            word_num[s[right]] += 1
            charmax = max(charmax, word_num[s[right]])
            if right - left + 1 > charmax + k:
                word_num[s[left]] -= 1
                left += 1
        return n - left
