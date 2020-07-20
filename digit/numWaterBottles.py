class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        while numBottles // numExchange != 0:
            new, left = divmod(numBottles, numExchange)
            result += new
            numBottles = new + left
        return result


k = Solution()
print(k.numWaterBottles(2, 3))
