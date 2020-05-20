class Solution:
    def magicalString(self, n: int) -> int:
        if n==0:return 0
        string = '122'
        i = 2
        char = 2
        ones=1
        while len(string) < n:
            char = 2 - char // 2
            if char==1:
                ones+=int(string[i])
            string += int(string[i])*str(char)
            i+=1
        print(string)
        print(len(string))
        return ones-1 if char==1 and len(string)>n else ones
k=Solution()
print(k.magicalString(13))