# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k==1 or not head or not head.next:
            return head
        record=cursor=ListNode(0)
        cursor.next=head
        while head:
            n=k
            end=head
            load=[]
            while n>0:
                load.append(end)
                end=end.next
                n -= 1
                if not end and n!=0:
                    return record.next
            while load and n==0:
                node=load.pop(-1)
                cursor.next=node
                cursor=cursor.next
            cursor.next=end
            head=end
        return record.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 所谓的颠翻转其实可以理解为，规定指向下一轮k个节点的指针h，将后面顺序遍历到的k个节点依次放到h.next，这样就可以达到翻转的效果

        # 返回第k个节点，作为下一次翻转的头节点h
        def pair_rev(h) -> ListNode:
            # 记下此段的第一个节点记为f，需要前置的节点是f.next(即节点g)
            f = h.next
            for _ in range(k - 1):
                g = f.next
                f.next = g.next
                g.next = h.next
                h.next = g
            return f

        # 得到链表的长度，进而得到需要翻转的次数
        flag, n = head, 0
        while flag:
            flag = flag.next
            n += 1
        times = n // k

        # 新建一个节点指向链表
        a = ListNode(-1)
        a.next = head
        # 执行times次
        for _ in range(times):
            h0 = pair_rev(a)
        return a.next



class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next

        return hair.next





L5=ListNode(5)
L4=ListNode(4)
L4.next=L5
L3=ListNode(3)
L3.next=L4
L2=ListNode(2)
L2.next=L3
L1=ListNode(1)
L1.next=L2


k=Solution()
b=k.reverseKGroup(L1,3)
while b!=None:
    print(b.val)
    b=b.next
