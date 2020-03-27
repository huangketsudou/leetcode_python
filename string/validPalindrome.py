class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        if n < 2: return True
        left, right = 0, n - 1
        flag = True
        while left <= right:
            if flag and s[left] != s[right]:
                left += 1
                flag = False
                continue
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                break
        if left > right: return True
        left, right = 0, n - 1
        flag = True
        while left <= right:
            if flag and s[left] != s[right]:
                right -= 1
                flag = False
                continue
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                break
        return True if left>right else False



class Solution:
    #贪心算法
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                case1, case2 = s[l:r], s[l+1:r+1]
                return case1 == case1[::-1] or case2 == case2[::-1]
            l, r = l+1, r-1
        return True



k=Solution()
print(k.validPalindrome('abcdba'))
