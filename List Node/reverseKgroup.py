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
