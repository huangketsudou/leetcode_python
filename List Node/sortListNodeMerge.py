from typing import List
import functools


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None  # 切断
        left, right = self.sortList(head), self.sortList(mid)
        h = res = ListNode(float('-inf'))
        while left and right:
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right
        return res.next


class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        h, length, inv = head, 0, 1
        while h: h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        while inv < length:
            pre, h = res, res.next
            while h:
                h1, i = h, inv
                while i and h:
                    h, i = h.next, i - 1
                    if i: break
                h2, i = h, inv
                while i and h:
                    h = h.next, i - 1
                c1, c2 = inv, inv - i
                while c1 and c2:
                    if h1.val < h2.val:
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else:
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0:
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h
            inv *= 2
        return res.next
