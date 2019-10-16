class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer=''
        if numRows==1:#error occur
            return s
        freq=2*(numRows-1)
        length=len(s)
        # maxK=length//freq+1
        for i in range(numRows):
            # k=0
            # while k<=maxK:
            #     index=k*freq
            #     if i==0 or i==numRows-1:
            #         if index+i<length:
            #             answer+=s[index+i]
            #     else:
            #         if length>index-i>0:
            #             answer+=s[index-i]
            #         if index+i<length:
            #             answer+=s[index+i]
            #     k+=1
            #-----------------------------
            j=0
            while j+i<length:
                answer+=s[j+i]
                if i!=0 and i!=numRows-1 and j+freq-i<length:
                    answer+=s[j+freq-i]
                j+=freq
        return answer


k=Solution()
print(k.convert('ABCDE',4))
