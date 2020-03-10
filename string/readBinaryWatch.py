class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        return [f"{h}:{m:02d}" for h in range(12) for m in range(60) if (bin(h)+bin(m)).count('1') == num]
    
    
#找到小时与分钟的二进制1的位数为num就加入结果中，从结果出发

