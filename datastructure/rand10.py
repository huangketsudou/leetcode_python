def rand7():
    x = 1
    return x


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            idx = col + (row - 1) * 7
            if idx <= 40:
                return 1 + (idx - 1) % 10
