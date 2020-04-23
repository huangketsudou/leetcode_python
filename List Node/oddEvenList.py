class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        RO=ODD=ListNode(-1)
        RE=EVEN=ListNode(-1)
        count=1
        while head:
            if count & 1:
                RO.next=head
                RO=RO.next
            else:
                RE.next=head
                RE=RE.next
            head=head.next
            count+=1
        RE.next=None
        RO.next=EVEN.next
        return ODD.next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p=head
        t=q=p.next
        while q and q.next:
            p.next,q.next=p.next.next,q.next.next
            p,q=p.next,q.next
        p.next=t
        return head


l1=ListNode(1)
l2=ListNode(2)
l3=ListNode(3)
l4=ListNode(4)
l5=ListNode(5)
# l6=ListNode(6)
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
# l5.next=l6


k=Solution()
b=k.oddEvenList(l1)
while b:
    print(b.val)
    b=b.next