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


#https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode/
#重要的分析过程
class Solution(object):
    def getIntersect(self, head):
        tortoise = head
        hare = head

        # A fast pointer will either loop around a cycle and meet the slow
        # pointer or reach the `null` at the end of a non-cyclic list.
        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if tortoise == hare:
                return tortoise

        return None

    def detectCycle(self, head):
        if head is None:
            return None

        # If there is a cycle, the fast/slow pointers will intersect at some
        # node. Otherwise, there is no cycle, so we cannot find an e***ance to
        # a cycle.
        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        # To find the e***ance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1
