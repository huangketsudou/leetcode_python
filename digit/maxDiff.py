class Solution:
    def maxDiff(self, num: int) -> int:
        if num==0:return 8
        strnum = str(num)
        n = len(strnum)
        i = 0
        while i<n and strnum[i] == '9':
            i += 1
        a = strnum.replace(strnum[i], '9') if i < n else strnum
        if strnum[0]!='1':
            b=strnum.replace(strnum[0],'1')
        else:
            i=1
            while i<n and (strnum[i]=='0' or strnum[i]=='1'):
                i+=1
            b=strnum.replace(strnum[i], '0') if i < n else strnum
        return int(a)-int(b)


k=Solution()
print(k.maxDiff(1101057))