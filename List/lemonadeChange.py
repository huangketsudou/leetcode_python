class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        profit={5:0,10:0,20:0}
        for v,i in enumerate(bills):
            if i!=5:
                if profit[5]<1:return False
                if i==20:
                    if profit[10]>0:
                        profit[10]-=1
                    elif profit[5]>2:
                        profit[5]-=2
                    else:
                        return False
                    profit[10]-=1
                profit[5]-=1
            profit[i]+=1
        return True

class Solution(object): #aw
    def lemonadeChange(self, bills):
        five = ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True



k=Solution()
print(k.lemonadeChange([5,5,10,20,5,5,5,5,5,5,5,5,5,10,5,5,20,5,20,5]))
