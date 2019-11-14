from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    #非原地修改
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:return head
        record=newhead=ListNode(0)
        while head!=None:
            count=0
            while head.next!=None and head.val==head.next.val:
                head=head.next
                count+=1
            if count==0:
                newhead.next=head
                newhead=newhead.next
            head=head.next
        newhead.next=None

        return record.next


class Solution2:
    def deleteDuplicates(self,head):
        if head is None:return head
        record=newhead=ListNode(0)
        newhead.next=head
        cursor=head
        while cursor!=None:
            count=0
            while cursor.next!=None and cursor.val==cursor.next.val:
                count+=1
                cursor=cursor.next
            if count==0:
                #无重复
                newhead.next=cursor
                newhead=newhead.next
                cursor=cursor.next
            else:
                #有重复
                cursor=cursor.next
                newhead.next=cursor

        return record.next













k=Solution2()
# L51=ListNode(5)
L5=ListNode(5)
# L5.next=L51
L4=ListNode(4)
L4.next=L5
L41=ListNode(4)
L41.next=L4
L3=ListNode(3)
L3.next=L41
L31=ListNode(3)
L31.next=L3
L2=ListNode(2)
L2.next=L31
L1=ListNode(1)
L1.next=L2
a=k.deleteDuplicates(L1)
while a:
    print(a.val)
    a=a.next

