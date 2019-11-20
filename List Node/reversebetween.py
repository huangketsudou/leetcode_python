from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n: return head
        mhead = record = ListNode(-1)
        record.next = head
        nhead  = head
        i = 0
        while i < n:
            if i > n - m:
                mhead=mhead.next
            nhead = nhead.next
            i += 1
        tmp=[]
        thead=mhead.next
        while thead!=nhead:
            tmp.append(thead)
            thead=thead.next
        while tmp:
            mhead.next=tmp.pop(-1)
            mhead=mhead.next
        mhead.next=nhead
        return record.next


class Solution2:
    # 递归版本
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 全局变量
        self.successor = None
        # 反转前N个节点函数
        def reverseN(head, n):
            if n == 1:
                self.successor = head.next
                return head
            last = reverseN(head.next, n-1)
            head.next.next = head
            head.next = self.successor
            return last
        if m == 1:
            return reverseN(head,n)
        head.next = self.reverseBetween(head.next, m-1, n-1)
        return head




class Solution3:
    # 非递归版本
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 重点是找到m前一个pre
        cur = head
        pre = None
        tail = None
        cnt = 0
        while cur:
            cnt += 1
            pre = cur if cnt == m - 1 else pre
            tail = cur if cnt == n + 1 else tail
            cur = cur.next
        if m > n or m < 1 or n > cnt:
            return head
        start = head if pre is None else pre.next
        cur = start.next
        start.next = tail
        # 反转逻辑
        while cur != tail:
            next = cur.next
            cur.next = start
            start = cur
            cur = next
        if pre:
            pre.next = start
            return head
        return start

L5=ListNode(5)
L4=ListNode(4)
L4.next=L5
L3=ListNode(3)
L3.next=L4
L2=ListNode(2)
L2.next=L3
L1=ListNode(1)
L1.next=L2


k = Solution()
a=k.reverseBetween(L1,2,4)

while a:
    print(a.val)
    a=a.next
