class Solution2:
    def mergeTwoLists(self, l1, l2):
        # maintain an unchanging reference to node ahead of the return node.
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next

        # exactly one of l1 and l2 can be non-null at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        Newhead=None
        record=None
        head=None
        while l1 or l2:
            if l1 and (l2==None or l1.val<l2.val):
                head = l1
                l1=l1.next
            elif l2 and (l1==None or l1.val>=l2.val):
                head=l2
                l2=l2.next
            if Newhead is None:
                record=Newhead=head
            else:
                Newhead.next=head
                Newhead=head
        return record


# L14=ListNode(1)
# L12=ListNode(1)
# L12.next=L14
# L11=ListNode(1)
# L11.next=L12
L11=None

L24=ListNode(1)
L23=ListNode(1)
L23.next=L24
L21=ListNode(1)
L21.next=L23

k=Solution()
result=k.mergeTwoLists(L11,L21)



while result!=None:
    print(result.val)
    result=result.next
