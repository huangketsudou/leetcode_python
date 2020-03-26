class Solution:
    def singleNumber(self, nums: List) -> List[int]:
        # difference between two numbers (x and y) which were seen only once
        bitmask = 0
        for num in nums:
            bitmask ^= num

        # rightmost 1-bit diff between x and y
        diff = bitmask & (-bitmask)
        #bitmask最右边的1要么来自x，要么来自y，x & （-x）的操作可以保留最右边的1
        #通过diff标记可以找到其中一个，另一个就是bitmask ^ x

        x = 0
        for num in nums:
            # bitmask which will contain only x
            #注意也存在其他数与bitmask与的结果为1，但这些数会出现两次，被异或掉了
            if num & diff:
                x ^= num

        return [x, bitmask ^ x]


