from typing import List
import functools


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:return False
        slow=head.next
        fast=head.next.next
        while slow and fast:
            if slow==fast:
                return True
            slow=slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break
        return False


N1=ListNode(1)
N2=ListNode(2)
N3=ListNode(3)
N4=ListNode(4)
N5=ListNode(5)
N1.next=N2
N2.next=N3
N3.next=N4
N4.next=N5
N5.next=N1

k=Solution()
print(k.hasCycle(N1))
