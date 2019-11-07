from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        #超时，k可以很大
        if not head:return None
        start=end=head
        while k>0:
            end=end.next
            if end==None:end=head
            k-=1
        if end==start:
            return head
        while end.next:
            end=end.next
            start=start.next
        newhead=start.next
        end.next=head
        start.next=None
        return newhead


class Solution2:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # base cases
        if not head:
            return None
        if not head.next:
            return head

        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head

        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for i in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next

        # break the ring
        new_tail.next = None

        return new_head




# L5=ListNode(5)
# L4=ListNode(4)
# L4.next=L5
# L3=ListNode(3)
# L3.next=L4
# L2=ListNode(2)
# L2.next=L3
# L1=ListNode(1)
# L1.next=L2


L2=ListNode(2)
L1=ListNode(1)
L1.next=L2
L0=ListNode(0)
L0.next=L1

k=Solution()
new=k.rotateRight(L0,3)


while new!=None:
    print(new.val)
    new=new.next
