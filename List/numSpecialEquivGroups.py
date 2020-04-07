class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        return len({(''.join(sorted(str[::2]) +sorted(str[1::2]))) for str in A})


class Solution(object):
    def numSpecialEquivGroups(self, A):
        def count(A):
            ans = [0] * 52
            for i, letter in enumerate(A):
                ans[ord(letter) - ord('a') + 26 * (i%2)] += 1
            return tuple(ans)

        return len({count(word) for word in A})

