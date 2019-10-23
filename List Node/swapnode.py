# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        record=cursor=ListNode(0)
        cursor.next=head
        while cursor.next!=None:
            nextNode=cursor.next
            if nextNode.next==None:
                break
            next2Node=nextNode.next
            cursor.next=next2Node
            nextNode.next=next2Node.next
            next2Node.next=nextNode
            cursor=nextNode

        return record.next
