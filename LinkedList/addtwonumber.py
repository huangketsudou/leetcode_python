class ListNode:
    def __init__(self,x):
        self.x=x
        self.next=None


class Solution:


    def addTwoNumbers(self,l1,l2):
        carry=0
        tmphead=ListNode(1000)
        record=tmphead
        while l1 or l2:
            x=l1.x if l1 else 0
            y=l2.x if l2 else 0
            summary=x+y+carry
            carry=summary//10
            if carry:
                tmphead.next=ListNode(summary-10)
            else:
                tmphead.next=ListNode(summary)
            tmphead = tmphead.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        if carry:
            tmphead.next=ListNode(1)
        return record.next



a1=ListNode(9)
a2=ListNode(9)
a2.next=a1
a3=ListNode(9)
a3.next=a2
a4=ListNode(2)
a4.next=a3

b1=ListNode(1)
b2=ListNode(1)
b2.next=b1
b3=ListNode(1)
b3.next=b2

k=Solution()

k=k.addTwoNumbers(a4,b3)

while k:
    print(k.x)
    k=k.next
