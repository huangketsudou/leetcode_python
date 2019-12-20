from typing import List
import functools


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head: return head
        pawn = ListNode(float('-inf'))
        pawn.next = head
        cur = head
        prev = pawn
        while cur:
            next = cur.next
            if prev.val<=cur.val:
                prev=cur
                cur=next
                continue
            node = pawn
            while node != cur:
                if cur.val >= node.val and cur.val < node.next.val:
                    cur.next = node.next
                    node.next = cur
                    prev.next = next
                    break
                else:
                    node = node.next
            cur=next
        return pawn.next




L4=ListNode(4)
L2=ListNode(2)
L1=ListNode(1)
L3=ListNode(3)
# L4.next=L2
# L2.next=L1
# L1.next=L3


k=Solution()
g=k.insertionSortList(None)

while g:
    print(g.val)
    g=g.next
