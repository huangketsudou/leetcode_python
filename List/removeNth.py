# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n==0:
            return head
        Newhead = pretail = cursor = head
        while n>0 and cursor.next!=None:
            cursor=cursor.next
            n-=1
        if n!=0:
            return Newhead.next
        while cursor.next!=None:
            cursor=cursor.next
            pretail=pretail.next
        pretail.next=pretail.next.next
        return Newhead


k = Solution()
L5=ListNode(5)
L4=ListNode(4)
L4.next=L5
L3=ListNode(3)
L3.next=L4
L2=ListNode(2)
L2.next=L3
L1=ListNode(1)
L1.next=L2

result=k.removeNthFromEnd(L1,5)
a=result
while a!=None:
    print(a.val)
    a=a.next
