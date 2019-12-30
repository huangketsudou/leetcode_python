
class Solution:
    def trailingZeroes(self, n: int) -> int:
        answer=0
        while n:
            answer+=n//5
            n//=5
        return answer

#数学规律题，10的出现为2*5，找到5就找到了10，5每5个数出现一次，每25个数出现2次，125个数出现3次，以此类推



k=Solution()
print(k.trailingZeroes(10))
